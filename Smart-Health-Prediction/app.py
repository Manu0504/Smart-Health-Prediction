# import streamlit as st
# import pickle
# import numpy as np

# # ------------------------------
# # Load models and scalers
# # ------------------------------
# with open("diabetes_model.pkl", "rb") as f:
#     diabetes_model = pickle.load(f)
# with open("diabetes_scaler.pkl", "rb") as f:
#     diabetes_scaler = pickle.load(f)

# with open("heart_model.pkl", "rb") as f:
#     heart_model = pickle.load(f)
# with open("heart_scaler.pkl", "rb") as f:
#     heart_scaler = pickle.load(f)

# with open("parkinsons_model.pkl", "rb") as f:
#     parkinsons_model = pickle.load(f)
# with open("parkinsons_scaler.pkl", "rb") as f:
#     parkinsons_scaler = pickle.load(f)

# # ------------------------------
# # Page config
# # ------------------------------
# st.set_page_config(page_title="Smart Health Prediction System", page_icon="🩺")
# st.title("🩺 Smart Health Prediction System")

# # Sidebar for disease selection
# disease = st.sidebar.selectbox(
#     "Select a Health Condition to Predict",
#     (
#         "🩸 Diabetes Prediction",
#         "❤️ Heart Disease Prediction",
#         "🧠 Parkinson's Disease Prediction"
#     )
# )

# # ------------------------------
# # Diabetes Section
# # ------------------------------
# if disease == "🩸 Diabetes Prediction":
#     st.subheader("Diabetes Prediction")
#     pregnancies = st.number_input("Pregnancies", min_value=0)
#     glucose = st.number_input("Glucose Level", min_value=0)
#     blood_pressure = st.number_input("Blood Pressure", min_value=0)
#     skin_thickness = st.number_input("Skin Thickness", min_value=0)
#     insulin = st.number_input("Insulin Level", min_value=0)
#     bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
#     diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
#     age = st.number_input("Age", min_value=0)

#     if st.button("Predict"):
#         features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
#         scaled = diabetes_scaler.transform(features)
#         prediction = diabetes_model.predict(scaled)
#         st.success("✅ Positive for Diabetes" if prediction[0] == 1 else "❌ Negative for Diabetes")

# # ------------------------------
# # Heart Disease Section
# # ------------------------------
# elif disease == "❤️ Heart Disease Prediction":
#     st.subheader("Heart Disease Prediction")
    
#     sex_map = {"Male": 1, "Female": 0}
#     cp_map = {
#         "Typical Angina (0)": 0,
#         "Atypical Angina (1)": 1,
#         "Non-anginal Pain (2)": 2,
#         "Asymptomatic (3)": 3
#     }
#     fbs_map = {"True (>120 mg/dl)": 1, "False": 0}
#     restecg_map = {
#         "Normal (0)": 0,
#         "ST-T wave abnormality (1)": 1,
#         "Left ventricular hypertrophy (2)": 2
#     }
#     exang_map = {"Yes": 1, "No": 0}
#     slope_map = {"Upsloping (0)": 0, "Flat (1)": 1, "Downsloping (2)": 2}
#     thal_map = {"Normal (0)": 0, "Fixed defect (1)": 1, "Reversible defect (2)": 2}

#     age = st.number_input("Age", min_value=0)
#     sex = sex_map[st.selectbox("Sex", list(sex_map.keys()))]
#     cp = cp_map[st.selectbox("Chest Pain Type", list(cp_map.keys()))]
#     trestbps = st.number_input("Resting Blood Pressure", min_value=0)
#     chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0)
#     fbs = fbs_map[st.selectbox("Fasting Blood Sugar > 120 mg/dl", list(fbs_map.keys()))]
#     restecg = restecg_map[st.selectbox("Rest ECG Results", list(restecg_map.keys()))]
#     thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
#     exang = exang_map[st.selectbox("Exercise Induced Angina", list(exang_map.keys()))]
#     oldpeak = st.number_input("ST Depression", format="%.1f")
#     slope = slope_map[st.selectbox("Slope of Peak Exercise ST Segment", list(slope_map.keys()))]
#     ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
#     thal = thal_map[st.selectbox("Thalassemia", list(thal_map.keys()))]

#     if st.button("Predict"):
#         features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
#                                oldpeak, slope, ca, thal]])
#         scaled = heart_scaler.transform(features)
#         prediction = heart_model.predict(scaled)
#         st.success("✅ Positive for Heart Disease" if prediction[0] == 1 else "❌ Negative for Heart Disease")

# # ------------------------------
# # Parkinson's Section
# # ------------------------------
# else:
#     st.subheader("Parkinson's Disease Prediction")
#     inputs = [
#         "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
#         "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
#         "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
#         "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"
#     ]
    
#     values = []
#     for label in inputs:
#         values.append(st.number_input(label, min_value=0.0))

#     if st.button("Predict"):
#         features = np.array([values])
#         scaled = parkinsons_scaler.transform(features)
#         prediction = parkinsons_model.predict(scaled)
#         st.success("✅ Positive for Parkinson's Disease" if prediction[0] == 1 else "❌ Negative for Parkinson's Disease")

import streamlit as st

st.set_page_config(page_title="Smart Health Prediction System", layout="centered")

st.title("🩺 Smart Health Prediction System")
st.markdown("Welcome! Use the sidebar to navigate between disease prediction and patient summary pages.")
