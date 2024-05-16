import streamlit as st
import requests
import json

# Function to send requests to the API
def send_request(payload):
    url = "http://104.236.9.38:5001/invocations"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# Layout the Streamlit app
st.title('Customer Churn Prediction')

# User input fields
tenure = st.slider("Tenure", 0, 100, 51)
phone_service = st.selectbox("Phone Service", [0, 1])
contract = st.selectbox("Contract", ["One year", "Month-to-month", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", [0, 1])
payment_method = st.selectbox("Payment Method", ["Bank transfer (automatic)", "Mailed check", "Electronic check", "Credit card (automatic)"])
monthly_charges = st.slider("Monthly Charges", 0.0, 200.0, 60.15)
total_charges = st.slider("Total Charges", 0.0, 5000.0, 3077.0)
gender = st.selectbox("Gender", ["Female", "Male"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", [0, 1])
dependents = st.selectbox("Dependents", [0, 1])
multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic"])
online_security = st.selectbox("Online Security", ["Yes", "No"])
device_protection = st.selectbox("Device Protection", ["Yes", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No"])
online_backup = st.selectbox("OnlineBackup", ["Yes", "No"])

# Construct the payload
payload = {
    'inputs': {
        'tenure': tenure,
        'PhoneService': phone_service,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'OnlineBackup': online_backup
    }
}

# Button to send the payload to the API
if st.button('Predict Churn'):
    response = send_request(payload)
    st.write('Response:')
    st.json(response)  # Display the raw JSON response for debugging or verification

    # Assuming the response contains a 'prediction' key and its value is a list with at least one item
    try:
        churn_prediction = response['predictions'][0]
        if churn_prediction == 1:
            st.success('Customer will churn')
        else:
            st.success('Customer will not churn')
    except (KeyError, IndexError, TypeError):
        st.error('Failed to retrieve prediction from response. Please check the API and the response format.')

# Run the Streamlit app by navigating to the directory containing the script
# and run: streamlit run app.py

