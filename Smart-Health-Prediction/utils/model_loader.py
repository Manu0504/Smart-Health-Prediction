# import pickle

# def load_model_and_scaler(model_path, scaler_path):
#     with open(model_path, "rb") as f:
#         model = pickle.load(f)
#     with open(scaler_path, "rb") as f:
#         scaler = pickle.load(f)
#     return model, scaler

import os
import pickle

# Get the project root directory (where app.py is located)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_model_and_scaler(model_filename, scaler_filename):
    """
    Loads a model and scaler from the models folder using absolute paths.
    
    Args:
        model_filename (str): The filename of the model (e.g., 'diabetes_model.pkl')
        scaler_filename (str): The filename of the scaler (e.g., 'diabetes_scaler.pkl')
    
    Returns:
        tuple: (model, scaler)
    """
    model_path = os.path.join(BASE_DIR, "models", model_filename)
    scaler_path = os.path.join(BASE_DIR, "models", scaler_filename)

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler
