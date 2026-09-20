import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.joblib")

st.title("Customer Churn Predictor")

gender = st.selectbox("Gender", ["Female", "Male"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0)
TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, value=1000.0)
SeniorCitizen_input = st.selectbox("Senior Citizen", ["No", "Yes"])
SeniorCitizen = 1 if SeniorCitizen_input == "Yes" else 0
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["No", "Yes"])
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
MultipleLines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

# Recreate engineered features from raw inputs
if tenure <= 12:
    TenureBucket = "0-12"
elif tenure <= 24:
    TenureBucket = "13-24"
elif tenure <= 48:
    TenureBucket = "25-48"
else:
    TenureBucket = "49+"

service_inputs = [PhoneService, OnlineSecurity, OnlineBackup,
                  DeviceProtection, TechSupport, StreamingTV, StreamingMovies]
ServiceCount = sum(1 for s in service_inputs if s == "Yes")

ChargePerTenureMonth = TotalCharges / tenure if tenure > 0 else 0

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "TenureBucket": TenureBucket,
        "ServiceCount": ServiceCount,
        "ChargePerTenureMonth": ChargePerTenureMonth
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == "Yes":
        st.error(f"High churn risk — {probability:.0%} probability")
    else:
        st.success(f"Low churn risk — {probability:.0%} probability")