import streamlit as st
from model import predict_number

st.title("AI Number Predictor")

number = st.number_input("Enter a number")

if st.button("Predict"):

    result = predict_number(number)

    st.success(result)