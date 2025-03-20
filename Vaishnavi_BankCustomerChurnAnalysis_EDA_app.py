import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open("ChurnAnalysis_Model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("Customer Churn Prediction App")

# Input fields for the user to enter customer details
customer_id = st.text_input("Customer ID")
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
account_tenure = st.number_input("Account Tenure (Years)", min_value=0, max_value=50, value=5)
account_type = st.selectbox("Account Type", ["Savings", "Current"])
balance_amount = st.number_input("Balance Amount", min_value=0.0, value=5000.0)
num_transactions = st.number_input("Number of Transactions per Month", min_value=0, value=10)
avg_transaction_value = st.number_input("Average Transaction Value", min_value=0.0, value=100.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
has_loan = st.selectbox("Has Loan?", ["Yes", "No"])
num_complaints = st.number_input("Number of Complaints Last Year", min_value=0, value=1)
satisfaction_score = st.slider("Satisfaction Score", min_value=1, max_value=10, value=5)
num_calls_customer_service = st.number_input("Number of Calls to Customer Service", min_value=0, value=2)
resolved_issues_percentage = st.slider("Resolved Issues Percentage", min_value=0, max_value=100, value=80)

# Convert categorical data to numerical
gender = 1 if gender == "Male" else 0
account_type = 1 if account_type == "Current" else 0
has_loan = 1 if has_loan == "Yes" else 0

# Prepare input for model
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender],
    'Account_Tenure': [account_tenure],
    'Account_Type': [account_type],
    'Balance_Amount': [balance_amount],
    'Num_Transactions_per_Month': [num_transactions],
    'Avg_Transaction_Value': [avg_transaction_value],
    'Credit_Score': [credit_score],
    'Has_Loan': [has_loan],
    'Num_Complaints_Last_Year': [num_complaints],
    'Satisfaction_Score': [satisfaction_score],
    'Num_Calls_Customer_Service': [num_calls_customer_service],
    'Resolved_Issues_Percentage': [resolved_issues_percentage]
})

# Predict churn
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    result = "Likely to Churn" if prediction == 1 else "Not Likely to Churn"
    st.subheader(f"Prediction: {result}")
