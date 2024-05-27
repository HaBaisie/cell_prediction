# Streamlit App: Using the Saved Model

import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("linear_regression_model.pkl")

# Streamlit app
st.title("Cell Width Prediction")

# Input features
catalase_test = st.number_input("Catalase Test Result", min_value=0, max_value=20, value=0)
oxidase_test = st.number_input("Oxidase Test Result", min_value=0, max_value=20, value=0)
maltose = st.number_input("Maltose Fermentation", min_value=0, max_value=20, value=0)
indole_test = st.number_input("Indole Test Result", min_value=0, max_value=20, value=0)
methyl_red_test = st.number_input("Methyl Red Test Result", min_value=0, max_value=20, value=0)
voges_proskauer_test = st.number_input("Voges Proskauer Test Result", min_value=0, max_value=20, value=0)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'const': [1],  # Add constant for intercept
    'CatalaseTest': [catalase_test],
    'OxidaseTest': [oxidase_test],
    'Maltose': [maltose],
    'IndoleTest': [indole_test],
    'MethylRedTest': [methyl_red_test],
    'VogesProskauerTest': [voges_proskauer_test]
})

# Predict CellWidth
if st.button("Predict"):
    cell_width_pred = model.predict(input_data)[0]
    st.write(f"Predicted Cell Width: {cell_width_pred:.2f}")
