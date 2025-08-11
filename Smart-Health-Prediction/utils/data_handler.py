import pandas as pd
import os

DATA_FILE = "data.txt"
COLUMNS = ["Name", "Address", "Disease", "Result"]

def load_patient_data():
    """Load patient data from CSV, create if missing or empty."""
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        # Create empty file with headers
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(DATA_FILE, index=False)
        return df
    try:
        return pd.read_csv(DATA_FILE)
    except pd.errors.EmptyDataError:
        # If file exists but has no data, reinitialize
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(DATA_FILE, index=False)
        return df

def save_patient_data(name, address, disease, result):
    """Save or update patient record in CSV."""
    df = load_patient_data()

    # Check if patient with same name & address exists
    mask = (df["Name"] == name) & (df["Address"] == address)

    if mask.any():
        # If same disease exists, update result
        disease_mask = mask & (df["Disease"] == disease)
        if disease_mask.any():
            df.loc[disease_mask, "Result"] = result
        else:
            # Add new disease record for same patient
            df = pd.concat(
                [df, pd.DataFrame([[name, address, disease, result]], columns=COLUMNS)],
                ignore_index=True
            )
    else:
        # Completely new patient record
        df = pd.concat(
            [df, pd.DataFrame([[name, address, disease, result]], columns=COLUMNS)],
            ignore_index=True
        )

    df.to_csv(DATA_FILE, index=False)
