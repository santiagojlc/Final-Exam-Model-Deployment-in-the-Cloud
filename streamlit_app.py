import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

def generate_forecast(model, year):
    # Generate forecast for the given year using the model
    # Replace this with your actual code to generate the forecast
    forecast = np.random.randn(10)  # Dummy forecast for demonstration
    return forecast

st.title("Daily Temperatures with Artificial Warming")

file_path = r'C:\Users\HP\Desktop\STREAMLIT\my_arima_model.h5'
model = load_model(file_path)

# Display forecast for each year
for year in range(2022, 2030):  # Adjust the range based on your requirement
    st.header(f"Forecast for Year {year}")
    forecast = generate_forecast(model, year)
    st.write(f"Forecast for Year {year}: {forecast}")
