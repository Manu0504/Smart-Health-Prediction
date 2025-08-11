🩺 Smart Health Prediction System
An AI-powered health assessment tool that predicts the risk of Diabetes, Heart Disease, and Parkinson’s Disease using patient health metrics.
Built with Machine Learning, Streamlit, and real-world datasets from Kaggle, this system provides instant predictions to aid early diagnosis and preventive care.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Features
Predict three major diseases: Diabetes, Heart Disease, and Parkinson’s Disease.
User-friendly web interface with dropdowns and number inputs.
Separate preprocessing & scaling for each disease for higher accuracy.
Uses real-world medical datasets from Kaggle.
Fully compatible with Google Colab and VS Code.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

📊 Datasets Used

Diabetes: Pima Indians Diabetes Database – Kaggle
Heart Disease: UCI Heart Disease Dataset – Kaggle
Parkinson’s Disease: UCI Parkinson’s Dataset – Kaggle

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛠 Tech Stack

Language: Python 3
Frontend: Streamlit
Backend: Scikit-learn
IDE: Google Colab / VS Code
Database (optional): MySQL for storing user data

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 Project Structure

Smart-Health-Prediction/
│
├── diabetes_model.pkl
├── diabetes_scaler.pkl
├── heart_model.pkl
├── heart_scaler.pkl
├── parkinsons_model.pkl
├── parkinsons_scaler.pkl
├── app.py               # Streamlit UI
├── README.md            # Project Documentation
└── requirements.txt     # Dependencies

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚡ Installation & Usage

1️. Clone the Repository

  git clone https://github.com/yourusername/smart-health-prediction.git
       cd smart-health-prediction

2️. Install Dependencies

  pip install -r requirements.txt

3️. Run the Application

  streamlit run app.py

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 How It Works

1. Select the disease you want to check from the sidebar.
2. Enter patient health details in the provided fields.
3. Click Predict to get instant results.
4. The system uses trained ML models to give a probability of disease.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

📈 Model Performance (Example)
______________________________
| Disease     | 	Accuracy    |
|_____________|_______________|
| Diabetes	  |   78%         |
|-----------------------------|           
|Heart Disease|	  85%         |
|-----------------------------| 
|Parkinson’s	|   87%         |
-------------------------------

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork and submit pull requests.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

📜 License
This project is licensed under the MIT License – free to use and modify.   
