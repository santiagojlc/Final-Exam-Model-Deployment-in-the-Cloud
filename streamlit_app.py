import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    # Setting up the plot with a warm background color
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#FFDAB9')  # Warm background color
    ax.set_facecolor('#FFE4B5')  # Light warm color for plot background
    ax.plot(data['date'], data['temperature'], color='skyblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature')
    ax.set_title('Daily Temperatures with Artificial Warming')
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.set_xticks(pd.date_range(start='2014-01-01', end='2017-12-31', freq='YS').to_pydatetime())
    ax.set_xticklabels([str(year) for year in range(2014, 2018)])
    st.pyplot(fig)
elif navigation == "About":
    st.write("About this app.")
