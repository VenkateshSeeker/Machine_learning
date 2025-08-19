import joblib
import numpy as np
import streamlit as st

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction App")

area = st.number_input("Enter area (sqft)", min_value=500, max_value=10000, step=50)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 10, 2)

if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price: ₹ {prediction:,.2f}")
