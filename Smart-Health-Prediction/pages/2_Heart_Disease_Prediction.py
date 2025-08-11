import streamlit as st
import numpy as np
from utils.data_handler import save_patient_data
from utils.model_loader import load_model_and_scaler

# Load model and scaler
model, scaler = load_model_and_scaler("models/heart_model.pkl", "models/heart_scaler.pkl")

st.title("❤️ Heart Disease Prediction")

# Patient details
name = st.text_input("Patient Name")
address = st.text_area("Address")

# Feature inputs
age = st.number_input("Age", min_value=1)
gender = st.selectbox("Gender", ["Male", "Female"])
sex = 1 if gender == "Male" else 0
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=0)
chol = st.number_input("Cholesterol Level", min_value=0)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
fbs = 1 if fbs == "Yes" else 0
restecg = st.selectbox("Rest ECG Results (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
exang = 1 if exang == "Yes" else 0
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, format="%.1f")
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0=Normal, 1=Fixed Defect, 2=Reversible Defect)", [0, 1, 2])

if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                          exang, oldpeak, slope, ca, thal]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)
    result = "Positive" if prediction[0] == 1 else "Negative"
    st.success(f"✅ {result} for Heart Disease")
    save_patient_data(name, address, "Heart Disease", result)
