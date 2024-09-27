import dill as pickle
import numpy as np
import streamlit as st

pipeline = pickle.load(open('house_price_pred_pipeline.pkl', 'rb'))

st.title("Zameen.com House Price Prediction")

# Input fields for the user to provide data
area_sq_ft = st.number_input("Enter the area in sq ft:", min_value = 1, max_value = 200000, value = 1000)
num_of_bed_bath = st.number_input("Enter the number of bedrooms and bathrooms combined:", min_value = 1, max_value = 25, value = 3)

# Create an array from the input
test_input = np.array([area_sq_ft, num_of_bed_bath], dtype = object).reshape(1,2)

# Button to make predictions
if st.button('Predict Price'):
    log_prediction = pipeline.predict(test_input)
    actual_prediction = np.exp(log_prediction)
    
    # Display the predicted price
    st.write(f"Predicted house price (in rupees): {actual_prediction[0]:,.2f}")