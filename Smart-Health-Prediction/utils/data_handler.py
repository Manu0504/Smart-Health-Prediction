import pandas as pd
import os

DATA_FILE = "data.txt"

def load_patient_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Name", "Address", "Disease", "Result"])

def save_patient_data(name, address, disease, result):
    df = load_patient_data()
    
    mask = (df["Name"] == name) & (df["Address"] == address)
    if mask.any():
        if ((df["Disease"] == disease) & mask).any():
            df.loc[mask & (df["Disease"] == disease), "Result"] = result
        else:
            df = pd.concat([df, pd.DataFrame([[name, address, disease, result]], columns=df.columns)], ignore_index=True)
    else:
        new_row = pd.DataFrame([[name, address, disease, result]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
    
    df.to_csv(DATA_FILE, index=False)
