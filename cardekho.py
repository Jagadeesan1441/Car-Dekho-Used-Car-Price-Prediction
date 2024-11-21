import streamlit as st
import pickle
from PIL import Image
import numpy as np

# Load the model
path = r"C:\Users\nsjag\streamlit\env\Scripts\__pycache__\car.pkl"
with open(path, "rb") as file:
    model = pickle.load(file)

input_features = ["Max Power", "Year of Manufacture", "Width", "Kerb Weight", "km", "Acceleration", "Mileage", "Wheel Base", "city"]

# Define label encoding for cities
city_mapping = {
    "Bangalore": 0,
    "Chennai": 1,
    "Delhi": 2,
    "Hyderabad": 3,
    "Jaipur": 4,
    "Kolkata": 5
}

st.title("Used Car Price Prediction")
st.image(r"C:\Users\nsjag\OneDrive\Desktop\used_cars.webp")

st.sidebar.header("Input Parameters")
params = {}
params["city"] = st.sidebar.selectbox("City", list(city_mapping.keys()))
params["Year of Manufacture"] = st.sidebar.slider("Year of Manufacture", 1990, 2026, 2014)
params["Max Power"] = st.sidebar.slider("Max Power (in hp)", 50, 60, 150)
params["Width"] = st.sidebar.slider("Width (in mm)", 1000, 2500, 1800)
params["Wheel Base"] = st.sidebar.slider("Wheel Base (in mm)", 2000, 4000, 2000)
params["Kerb Weight"] = st.sidebar.slider("Kerb Weight (in kg)", 500, 3000, 1500)
params["km"] = st.sidebar.slider("km driven (in km)", 5000,100000, 1000)
params["Acceleration"] = st.sidebar.slider("Acceleration (0-100 km/h in sec)", 2, 15, 10)
params["Mileage"] = st.sidebar.slider("Mileage (in km/l)", 10, 150, 5)

# Convert city to numeric
params["city"] = city_mapping[params["city"]]

# Prepare input data
input_data = np.array([params[feature] for feature in input_features]).reshape(1, -1)

# Predict the price
predicted_price = model.predict(input_data)[0]

st.write(f"The Predicted Price is: ₹{predicted_price:.2f} lakhs")
