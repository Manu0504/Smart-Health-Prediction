import streamlit as st
import numpy as np
from utils.data_handler import save_patient_data
from utils.model_loader import load_model_and_scaler

# Load model and scaler
model, scaler = load_model_and_scaler("diabetes_model.pkl", "diabetes_scaler.pkl")

st.title("🧠 Parkinson's Disease Prediction")

# Patient details
name = st.text_input("Patient Name")
address = st.text_area("Address")

# Parkinson’s features (subset for simplicity)
fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, format="%.3f")
fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0, format="%.3f")
flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0, format="%.3f")
jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, format="%.6f")
jitter_abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, format="%.6f")
rap = st.number_input("MDVP:RAP", min_value=0.0, format="%.6f")
ppq = st.number_input("MDVP:PPQ", min_value=0.0, format="%.6f")
ddp = st.number_input("Jitter:DDP", min_value=0.0, format="%.6f")
shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, format="%.6f")
shimmer_db = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, format="%.6f")

if st.button("Predict"):
    features = np.array([[fo, fhi, flo, jitter_percent, jitter_abs,
                          rap, ppq, ddp, shimmer, shimmer_db]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)
    result = "Positive" if prediction[0] == 1 else "Negative"
    st.success(f"✅ {result} for Parkinson's Disease")
    save_patient_data(name, address, "Parkinson's Disease", result)

