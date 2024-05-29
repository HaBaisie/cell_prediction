import streamlit as st
import pandas as pd
import joblib

# Load the trained model and label encoder
model = joblib.load("bacterial_species_classifier.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Title of the Streamlit app
st.title("Bacterial Species Prediction")

# Collecting user input features
st.header("Input Features")
catalase_test = st.selectbox("Catalase Test (0 or 1)", [0, 1])
oxidase_test = st.selectbox("Oxidase Test (0 or 1)", [0, 1])
maltose = st.number_input("Maltose", min_value=0.0, step=0.1)
indole_test = st.selectbox("Indole Test (0 or 1)", [0, 1])
methyl_red_test = st.selectbox("Methyl Red Test (0 or 1)", [0, 1])
voges_proskauer_test = st.selectbox("Voges Proskauer Test (0 or 1)", [0, 1])
cell_width = st.number_input("Cell Width (in mm)", min_value=0.0, step=0.1)
cell_length = st.number_input("Cell Length (in mm)", min_value=0.0, step=0.1)
cell_shape = st.selectbox("Cell Shape (0 or 1)", [0, 1])  # Assuming cellShape is binary encoded

# Prediction button
if st.button("Predict Bacterial Species"):
    # Create a dataframe with the input features
    input_features = pd.DataFrame({
        'CatalaseTest': [catalase_test],
        'OxidaseTest': [oxidase_test],
        'Maltose': [maltose],
        'IndoleTest': [indole_test],
        'MethylRedTest': [methyl_red_test],
        'VogesProskauerTest': [voges_proskauer_test],
        'CellWidth': [cell_width],
        'CellLength': [cell_length],
        'cellShape': [cell_shape]
    })
    
    # Making predictions
    prediction = model.predict(input_features)
    
    # Decoding the prediction
    predicted_species = label_encoder.inverse_transform(prediction)[0]
    
    # Displaying the result
    st.subheader(f"The predicted bacterial species is: {predicted_species}")

# To run this Streamlit app, save the code in a file named `app.py` and use the command:
# streamlit run app.py
