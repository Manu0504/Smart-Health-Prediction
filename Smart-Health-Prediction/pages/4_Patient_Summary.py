import streamlit as st
from utils.data_handler import load_patient_data

st.title("📋 Patient Summary")

df = load_patient_data()

if df.empty:
    st.info("No patient records found.")
else:
    search_name = st.text_input("Search by Name or Address").lower()
    if search_name:
        df = df[df.apply(lambda row: search_name in row["Name"].lower() or search_name in row["Address"].lower(), axis=1)]
    st.dataframe(df)
