import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

st.title("Daily Temperatures with Artificial Warming")

model = load_model('my_arima_model.h5')
