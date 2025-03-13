# Grp6_Final-Project
Project Summary: AI-Powered Travel Recommendation System
Our project leverages machine learning and real-time API data to predict travel destinations based on user input and recommend hotels & attractions.
Model Training
We trained a Random Forest Classifier using a dataset that includes travel details such as:
Accommodation Cost
Traveler’s Age
Duration of Stay
The model was specifically trained to predict the most likely travel destination based on these three key factors.
Prediction & API Integration
When a user inputs their accommodation budget, age, and duration, our trained model predicts the most probable destination.
After predicting the destination, we integrate TripAdvisor’s API to pull real-time hotel and attraction recommendations.
Additionally, we use the Pexels API to fetch a relevant city image.
Key Insights
Accommodation cost played a major role in predicting destinations, meaning that travelers' budgets significantly influenced their predicted location.
The system provides dynamic, real-time travel recommendations, ensuring relevant and up-to-date results for users.
4:23
andrew, maybe we can keep relevant visuals that can show this info, the one where it says based on accommodation budget, duration and age
