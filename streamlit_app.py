import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Function to load the model
@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

# Load the model
model = load_model('smoothed_series.pkl')

# Function to generate temperature data using the model
def generate_temperature_data(model, start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    # Assuming the model can generate temperature data for the date range
    # Here we simulate it with random data, replace this with model predictions
    temperature_data = pd.DataFrame({
        'date': date_range,
        'temperature': np.random.uniform(low=10, high=18, size=len(date_range))  # Replace with model predictions
    })
    return temperature_data

st.title("Daily Temperatures with Artificial Warming")

# Generate data
data = generate_temperature_data(model, '2014-01-01', '2017-12-31')

# Adding navigation and other sections
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Explore", "About"])

if navigation == "Home":
    st.write("Welcome to the Home section.")
elif navigation == "Explore":
    st.subheader("Graph showing daily temperatures can be viewed below")
    fig, ax = plt.subplots()
    ax.plot(data['date'], data['temperature'], color='skyblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature')
    ax.set_title('Daily Temperatures with Artificial Warming')
    st.pyplot(fig)
elif navigation == "About":
    st.write("About this app.")
