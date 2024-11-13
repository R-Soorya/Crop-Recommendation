import pickle
import streamlit as st
import numpy as np

st.title("Crop Recommendation System")

model = pickle.load(open('RandomForest.pkl','rb'))

N = st.number_input("Nitrogen Content",min_value=0)
P = st.number_input("Phosphorous Content",min_value=0)
K = st.number_input("Potassium Content",min_value=0)
temperature = st.number_input("Temperature in Celcius")
humidity = st.number_input("Humidity in Air")
ph = st.number_input("pH of the Soil",min_value=0.00,max_value=14.00)
rainfall = st.number_input("Rainfall Measure",min_value=0.00,max_value=400.00)

if st.button("Predict"):
    data = np.array([[N,P,K,temperature,humidity,ph,rainfall]])
    prediction = model.predict(data)
    crop = prediction[0]
    crop = crop.upper()
    st.header(f"The suitable crop is : {crop}")