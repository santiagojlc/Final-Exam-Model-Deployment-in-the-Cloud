import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to load the dataset
@st.cache_data
def load_data():
    date_range = pd.date_range(start='2017-01-01', end='2017-07-31', freq='D')
    sales_data = pd.DataFrame({
        'date': date_range,
        'sales': np.random.poisson(lam=1000, size=len(date_range))
    })
    return sales_data

st.title("A Chart of the Daily Sales Across Favorita Stores")

# Load data
data = load_data()

# Plotting the data
st.subheader("Graph showing daily sales can be viewed below")
fig, ax = plt.subplots()
ax.plot(data['date'], data['sales'], color='skyblue')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Daily Sales Across Favorita Stores')
st.pyplot(fig)

# Adding navigation and other sections
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Forecast", "Explore", "About"])

if navigation == "Home":
    st.write("Welcome to the Home section.")
elif navigation == "Forecast":
    st.write("Forecasting section under development.")
elif navigation == "Explore":
    st.write("Explore the dataset and charts here.")
elif navigation == "About":
    st.write("About this app.")
