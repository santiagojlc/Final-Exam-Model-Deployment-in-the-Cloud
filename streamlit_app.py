import streamlit as st
import pandas as pd
import numpy as np

# Function to load the dataset
@st.cache_data
def load_data():
    date_range = pd.date_range(start='2014-01-01', end='2017-12-31', freq='D')
    temperature_data = pd.DataFrame({
        'date': date_range,
        'temperature': np.random.uniform(low=10, high=18, size=len(date_range))  # Example temperature data
    })
    return temperature_data

st.title("Daily Temperatures with Artificial Warming")

# Load data
data = load_data()

# Adding navigation and other sections
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Explore", "About"])

if navigation == "Home":
    st.write("Welcome to the Home section.")
elif navigation == "Explore":
    st.subheader("Graph showing daily temperatures can be viewed below")
    st.image("Graph.jfif", caption="Daily Temperatures with Artificial Warming", use_column_width=True)
elif navigation == "About":
    st.write("About this app.")
