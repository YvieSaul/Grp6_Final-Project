# Grp6_Final-Project

#### Jesus Mata
#### Yvette Saul
#### Ken Priest
#### Andrew Kliever


## Project Summary: AI-Powered Travel Recommendation System

Our project leverages machine learning and real-time API data to recommend travel destinations, hotels and attractions based on user input.

## Model Training
We trained a Random Forest Classifier using datasets acquired from Kaggle.  Datasets included travel details such as:
* Accommodation Cost
* Traveler’s Age
* Duration of Stay
* Gender
* Type of travel and accomodation

The model was specifically trained to predict the most likely travel destination based on the top three factors.

## Prediction & API Integration
When a user inputs their accommodation budget, age, and duration, our trained model predicts the most probable destination.
After predicting the destination, we integrate TripAdvisor’s API to pull real-time hotel and attraction recommendations.
Additionally, we use the Pexels API to fetch a relevant city image.

## Key Insights
Accommodation cost played a major role in predicting destinations, meaning that travelers' budgets significantly influenced their predicted location.
The system provides dynamic, real-time travel recommendations, ensuring relevant and up-to-date results for users.

## References:
* https://www.kaggle.com/datasets/rkiattisak/traveler-trip-data
* https://www.kaggle.com/datasets/midesowunmi/hotels-from-around-the-world
* https://www.kaggle.com/datasets/jahnavipaliwal/mountains-vs-beaches-preference
* TripAdvisor API
* PEXELS API

