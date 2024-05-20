import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from pathlib import Path
import os

# Load ARIMA model with error handling
@st.cache_resource
def load_arima_model(model_path):
    if model_path.exists():
        model = load_model(str(model_path))
        return model
    else:
        st.error(f"Model file not found: {model_path}")
        return None

# Function to load the dataset
@st.cache_data
def load_data():
    date_range = pd.date_range(start='2014-01-01', end='2017-12-31', freq='D')
    temperature_data = pd.DataFrame({
        'date': date_range,
        'temperature': np.random.uniform(low=10, high=18, size=len(date_range))  # Example temperature data
    })
    return temperature_data

# Function to predict future temperatures
@st.cache_data
def predict_temperatures(model, data, steps=60):
    if model is None:
        return []
    
    # Preprocess data if necessary
    last_data = data['temperature'].values[-steps:]
    last_data = last_data.reshape((1, -1, 1))  # Reshape for the model

    # Make predictions
    predictions = model.predict(last_data)
    return predictions.flatten()

# Load data and model
data = load_data('arima_model.pkl')

st.title("Temperatures with Artificial Warming")

# Adding navigation and other sections
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Explore", "About"])

if navigation == "Home":
    st.markdown("""
    <div style='text-align: justify;'>
    Welcome to our page! Here, we delve into the fascinating world of Detroit's Temperatures with Artificial Warming. Our focus lies in predicting and forecasting the temperature trends over the upcoming two months. Moreover, we keenly observe how global warming impacts these trends, offering insights into the evolving climate scenario. Join us as we analyze, predict, and visualize the temperature trends, empowering you with valuable insights into the future climate of this vibrant city.
    </div>
    """, unsafe_allow_html=True)
elif navigation == "Explore":
    st.subheader("Temperatures with Artificial Warming")

    if arima_model:
        # Predict future temperatures
        predictions = predict_temperatures(arima_model, data)

        if len(predictions) > 0:
            # Create a DataFrame for the predictions
            future_dates = pd.date_range(start=data['date'].iloc[-1] + pd.Timedelta(days=1), periods=len(predictions), freq='D')
            predictions_df = pd.DataFrame({'date': future_dates, 'predicted_temperature': predictions})

            # Plot the data
            plt.figure(figsize=(10, 6))
            plt.plot(data['date'], data['temperature'], label='Historical Temperatures')
            plt.plot(predictions_df['date'], predictions_df['predicted_temperature'], label='Predicted Temperatures', linestyle='--')
            plt.xlabel('Date')
            plt.ylabel('Temperature (°C)')
            plt.title('Temperature Predictions')
            plt.legend()
            plt.grid(True)
            
            # Display the plot
            st.pyplot(plt)
        else:
            st.warning("No predictions to display.")
    else:
        st.warning("Model could not be loaded. Please check the file path.")
elif navigation == "About":
    st.markdown("""
    <div style='text-align: justify;'>
    Through this platform, you'll embark on a journey through time and temperature, exploring the intricate interplay between artificial influences and natural climatic patterns. As we unravel the data, you'll gain a deeper understanding of the dynamic nature of Detroit's temperature landscape.
    </div>
    """, unsafe_allow_html=True)
