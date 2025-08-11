import streamlit as st
import numpy as np
from utils.data_handler import save_patient_data
from utils.model_loader import load_model_and_scaler

# Load model and scaler without hardcoding "models/"
model, scaler = load_model_and_scaler("diabetes_model.pkl", "diabetes_scaler.pkl")

st.title("🩸 Diabetes Prediction")

# Patient info
name = st.text_input("Patient Name")
address = st.text_area("Address")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=0)

# Prediction button
if st.button("Predict"):
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)
    result = "Positive" if prediction[0] == 1 else "Negative"
    st.success(f"✅ {result} for Diabetes")
    save_patient_data(name, address, "Diabetes", result)
