import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

st.title("TITLE")

model = load_model(r'C:\Users\HP\Desktop\STREAMLIT\my_arima_model.h5')

