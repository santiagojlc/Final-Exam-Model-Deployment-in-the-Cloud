import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

st.title("Daily Temperatures with Artificial Warming")

file_path = 'C:\Users\HP\Desktop\STREAMLIT\my_arima_model.h5'
model = load_model(file_path)

# Display information about the ARIMA model
st.write("ARIMA Model Details:")
st.write(model.summary())
