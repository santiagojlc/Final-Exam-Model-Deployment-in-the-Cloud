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

    # Displaying the graph
    st.pyplot(create_graph(data))
elif navigation == "About":
    st.write("About this app.")

# Function to create the graph
def create_graph(data):
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 6))
    gradient_colors = ['#FFDAB9', '#FFE4B5']  # Warm to cold gradient colors
    fig.patch.set_facecolor(gradient_colors[0])  # Set warm color as background
    ax.plot(data['date'], data['temperature'], color='skyblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature')
    ax.set_title('Daily Temperatures with Artificial Warming')
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.set_xticks(pd.date_range(start='2014-01-01', end='2017-12-31', freq='YS').to_pydatetime())
    ax.set_xticklabels([str(year) for year in range(2014, 2018)])
    return fig

# Applying warm-cold gradient background to the whole app
page_bg = '''
<style>
[data-testid="stApp"] {
    background: linear-gradient(to right, #FFDAB9, #FFE4B5);
    color: black;
}
</style>
'''

st.markdown(page_bg, unsafe_allow_html=True)
