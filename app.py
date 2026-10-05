
import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("diabetes_model.joblib")
scaler = joblib.load("scaler.joblib")

# Page configuration
st.set_page_config(
    page_title="Diabetes Progression Predictor",
    page_icon="🩺",
    layout="centered"
)

# Title
st.title("🩺 Diabetes Progression Predictor")

st.write(
    "Enter the patient features below to predict the diabetes "
    "disease progression score."
)

st.info(
    "This application is an educational machine-learning project "
    "and is not intended for medical diagnosis."
)

# Input features
age = st.number_input("Age", value=0.0, format="%.4f")
sex = st.number_input("Sex", value=0.0, format="%.4f")
bmi = st.number_input("BMI", value=0.0, format="%.4f")
bp = st.number_input("Blood Pressure (BP)", value=0.0, format="%.4f")
s1 = st.number_input("S1", value=0.0, format="%.4f")
s2 = st.number_input("S2", value=0.0, format="%.4f")
s3 = st.number_input("S3", value=0.0, format="%.4f")
s4 = st.number_input("S4", value=0.0, format="%.4f")
s5 = st.number_input("S5", value=0.0, format="%.4f")
s6 = st.number_input("S6", value=0.0, format="%.4f")

# Prediction button
if st.button("Predict Diabetes Progression"):

    input_data = np.array([[
        age, sex, bmi, bp, s1, s2, s3, s4, s5, s6
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    st.success(
        f"Predicted Diabetes Progression Score: {prediction:.2f}"
    )
