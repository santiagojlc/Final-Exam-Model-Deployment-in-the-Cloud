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

# Adding navigation and other sections
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Explore", "About"])

if navigation == "Home":
    st.markdown("""
    <div style='text-align: justify;'>
    Welcome to our page! Here, we delve into the fascinating world of Detroit's Daily Temperatures with Artificial Warming. Our focus lies in predicting and forecasting the temperature trends over the upcoming two months. Moreover, we keenly observe how global warming impacts these trends, offering insights into the evolving climate scenario.     Join us as we analyze, predict, and visualize the temperature trends, empowering you with valuable insights into the future climate of this vibrant city.
    </div>
    """, unsafe_allow_html=True)
elif navigation == "Explore":
    st.subheader("Daily Temperatures with Artificial Warming")
    st.image("Graph.jfif", caption="This graph presents the predictions and forecasts of daily temperatures in Detroit from 2012 to 2017 and beyond.", use_column_width=True)
elif navigation == "About":
    st.markdown("""
    <div style='text-align: justify;'>
    Through this platform, you'll embark on a journey through time and temperature, exploring the intricate interplay between artificial influences and natural climatic patterns. As we unravel the data, you'll gain a deeper understanding of the dynamic nature of Detroit's temperature landscape.
    </div>
    """, unsafe_allow_html=True)
