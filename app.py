import streamlit as st
import joblib
import numpy as np

# Load the scaler and model. Ensure these files ('scaler.pkl', 'model.pkl') are in the same directory.
try:
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("model.pkl")
except FileNotFoundError:
    st.error("Error: 'scaler.pkl' or 'model.pkl' not found. Please ensure these files are in the same directory.")
    st.stop() # Stop the app if essential files are missing

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

# Input fields for user data
age = st.number_input("Enter age", min_value=10, max_value=100, value=30)
tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
monthlycharge = st.number_input("Enter Monthly Charge", min_value=30, max_value=150)
gender = st.selectbox("Enter the Gender", ["Male", "Female"])

st.divider()

predictbutton = st.button("Predict!")

# Prediction logic
if predictbutton:
    # Convert gender to numerical format (0 for Male, 1 for Female)
    gender_selected = 1 if gender == "Female" else 0

    # Create a numpy array with the input features
    # The order of features here must match the order expected by your trained model
    X = [age, gender_selected, tenure, monthlycharge]
    X1 = np.array(X).reshape(1, -1) # Reshape for single sample prediction

    # Scale the input features using the loaded scaler
    X_array = scaler.transform(X1)

    # Make a prediction using the loaded model
    prediction = model.predict(X_array)[0]

    # Convert the numerical prediction to a human-readable string
    predicted = "Yes" if prediction == 1 else "No"

    # Display the prediction result
    st.write(f"Predicted: {predicted}")
else:
    # Message displayed when the app first loads or after a prediction
    st.write("Please enter the values and use Predict button")

