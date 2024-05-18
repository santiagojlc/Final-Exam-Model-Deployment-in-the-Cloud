import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

st.title("Water Quality Prediction")

model = load_model('C:\Users\HP\Desktop\STREAMLIT\my_arima_model.h5')

col1, col2, col3 = st.columns(3)

page_bg = '''
<style>
[data-testid="stAppViewContainer"] {
    background: rgba(0, 0, 0, 0) url("https://images.pexels.com/photos/1533720/pexels-photo-1533720.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: black;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
</style>
'''

st.markdown(page_bg, unsafe_allow_html=True)
