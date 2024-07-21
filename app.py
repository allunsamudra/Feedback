import streamlit as st
import joblib
import numpy as np

# Muat model yang sudah dilatih
model = joblib.load('onlinefood.pkl')

st.title("Iris Species Classifier")
st.write("Masukkan fitur-fitur dari bunga iris dan model akan memprediksi spesiesnya.")

Age = st.number_input("Age", min_value=0.0, max_value=100.0)
Gender = st.number_input("Gender", min_value=0.0, max_value=1.0)
Occupation = st.number_input("Occupation", min_value=0.0, max_value=4.0)
MonthlyIncome = st.number_input("MonthlyIncome", min_value=0.0, max_value=4.0)
EducationalQualifications = st.number_input("EducationalQualifications", min_value=0.0, max_value=3)

if st.button("Predict"):
    features = np.array([[(Age, Gender, Occupation, MonthlyIncome, EducationalQualifications]])
    prediction = model.predict(features)
    st.write(f"The predicted feedback is: {prediction[0]}")
