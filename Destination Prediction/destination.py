from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import requests

app = Flask(__name__)

TRIPADVISOR_API_KEY = "YOUR KEY"

# ==========================
# Load Model & Data
# ==========================
# Load trained Random Forest model
destination_model = joblib.load("destination_model.pkl")

# Load label encoder for decoding city names
label_encoder = joblib.load("label_encoder.pkl")

# Load global hotels dataset
global_hotels_df = pd.read_csv("global_hotels.csv")

# ==========================
# Flask Routes
# ==========================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Extract user inputs
    accommodation_cost = float(request.form.get("accommodation_cost", 500))  # Default to 500 if not provided
    age = int(request.form.get("age", 30))  # Default to 30
    duration = int(request.form.get("duration", 7))  # Default to 7

    # Prepare input for prediction
    model_input = [[accommodation_cost, age, duration]]

    # Predict destination
    predicted_destination_encoded = destination_model.predict(model_input)[0]

    # Decode prediction back to city name
    predicted_destination = label_encoder.inverse_transform([predicted_destination_encoded])[0]

    # Fetch 2 hotels from TripAdvisor
    hotels = get_tripadvisor_data(predicted_destination, "hotels")

    # Fetch 2 attractions from TripAdvisor
    attractions = get_tripadvisor_data(predicted_destination, "attractions")

    # Fetch an image of the predicted destination
    image_url = get_city_image_url(predicted_destination)

    # 🔥 DEBUGGING: Print data being sent to the HTML template
    print("=== Debugging Data Sent to HTML ===")
    print("Predicted Destination:", predicted_destination)
    print("Hotels Data:", hotels)
    print("Attractions Data:", attractions)

    return render_template("results.html", destination=predicted_destination, hotels=hotels, attractions=attractions, image_url=image_url)


def get_city_image_url(city):
    """
    Fetches an image URL of the city using the Pexels API.
    """
    PEXELS_ACCESS_KEY = "YOUR KEY"  # actual API key
    search_url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_ACCESS_KEY}
    params = {"query": city, "per_page": 1}

    try:
        response = requests.get(search_url, headers=headers, params=params)
        data = response.json()
        if data.get("photos"):
            return data["photos"][0]["src"]["medium"]
        else:
            return "https://via.placeholder.com/400?text=No+Image+Found"
    except Exception as e:
        print(f"Error fetching image: {e}")
        return "https://via.placeholder.com/400?text=Error+Fetching+Image"
    
def get_tripadvisor_data(city, category):
    """
    Fetches data (hotels or attractions) from TripAdvisor for a given city.
    """
    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key={TRIPADVISOR_API_KEY}&searchQuery={city}&category={category}&language=en"
    headers = {"accept": "application/json",}
    print(f"Requesting TripAdvisor API: {url}")
    
    params = {
        "searchQuery": city,
        "category": category,  # "hotels" or "attractions"
        "language": "en"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"TripAdvisor {category} API Response:", response.text) 
        data = response.json()
        
        if "data" in data and len(data["data"]) > 0:
            return [
                {
                    "name": item.get("name"),
                    "location": item["address_obj"]["address_string"],
                    "tripadvisor_url": item.get("web_url", "https://www.tripadvisor.com/")
                }
                for item in data["data"][:2]  # Get top 2 items
            ]
        else:
            return [{"message": f"No {category} found for {city}."}]
    except Exception as e:
        print(f"Error fetching {category}: {e}")
        return [{"message": f"Error fetching {category} from TripAdvisor."}]


if __name__ == '__main__':
    app.run(debug=True)
