import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
#MODEL_PATH = "rucha_water.pkl"  # Replace with the actual path to your .pkl file
MODEL_PATH = "waterquality.pkl"
try:
    with open(MODEL_PATH, 'rb') as file:
        water_quality_model = pickle.load(file)
    with open('water_level_model.pkl', 'rb') as f:
        water_level_model = pickle.load(f)

    with open('waterquality.pkl', 'rb') as f:
        water_quality_model = pickle.load(f)

    # with open('water_discharge_model.pkl', 'rb') as f:
    #     water_discharge_model = pickle.load(f)

    with open('hydro_drilling.pkl', 'rb') as f:
        drilling_technique_model = pickle.load(f)    
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'model.pkl' is in the correct path.")
    st.stop()

# Streamlit UI setup
st.title("AI-Enabled Water Well Prediction Model")
st.markdown("""
This application predicts water well suitability and related parameters based on geographical coordinates.
Please enter the latitude and longitude to get predictions.
""")

# Input fields
latitude = st.number_input("Enter Latitude (e.g., 25.2048):", format="%f")
longitude = st.number_input("Enter Longitude (e.g., 55.2708):", format="%f")

# Predict button
if st.button("Predict"):
    # Validate inputs
    if not (-90 <= latitude <= 90):
        st.error("Latitude must be between -90 and 90.")
    elif not (-180 <= longitude <= 180):
        st.error("Longitude must be between -180 and 180.")
    else:
        # Prepare input for the model
        input_data = np.array([[latitude, longitude]])
        
        # Make prediction
        try:
            water_level = water_level_model.predict(input_data)[0]
            water_quality = water_quality_model.predict(input_data)[0]
            #water_discharge = water_discharge_model.predict(input_data)[0]
            drilling_technique = drilling_technique_model.predict(input_data)[0]
            st.write("### Prediction Results:")
            st.success(f"**Water Level:** {water_level:.2f}")
            st.success(f"**Water Quality:** {water_quality:.2f}")
            #st.success(f"**Water Discharge:** {water_discharge:.2f}")
            st.success(f"**Drilling Technique:** {drilling_technique:.2f}")  # Adjust output format as needed
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")
            
