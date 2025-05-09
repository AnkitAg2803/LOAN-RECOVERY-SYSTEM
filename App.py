import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoders
model_rf = joblib.load("loan_default_model.joblib")
label_encoders = joblib.load("label_encoders.joblib")

# Define all features used during training
expected_features = [
    'Age', 'Gender', 'Employment_Type', 'Monthly_Income', 'Num_Dependents',
    'Loan_Amount', 'Loan_Tenure', 'Interest_Rate', 'Loan_Type', 'Collateral_Value',
    'Outstanding_Loan_Amount', 'Monthly_EMI', 'Payment_History',
    'Num_Missed_Payments', 'Days_Past_Due', 'Collection_Attempts',
    'Collection_Method', 'Legal_Action_Taken'
]

# Streamlit UI for minimal important inputs
st.title("💼 Smart Loan Default Prediction System")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=70)
employment_type = st.selectbox("Employment Type", ["Salaried", "Self-Employed", "Unemployed"])
monthly_income = st.slider("Monthly Income", 5000, 200000, step=1000)
loan_amount = st.slider("Loan Amount", 5000, 1400000, step=10000)
loan_tenure = st.number_input("Loan Tenure (months)", min_value=1)
interest_rate = st.slider("Interest Rate (%)", 5.0, 30.0, step=0.5)

# Create base input with user data
input_data = {
    'Age': age,
    'Gender': gender,
    'Employment_Type': employment_type,
    'Monthly_Income': monthly_income,
    'Loan_Amount': loan_amount,
    'Loan_Tenure': loan_tenure,
    'Interest_Rate': interest_rate
}

# Add default values for missing fields
default_values = {
    'Num_Dependents': 0,
    'Loan_Type': 1,
    'Collateral_Value': 0.0,
    'Outstanding_Loan_Amount': loan_amount,  # or 0.0
    'Monthly_EMI': (loan_amount / loan_tenure) if loan_tenure else 0,
    'Payment_History': 1,
    'Num_Missed_Payments': 0,
    'Days_Past_Due': 0,
    'Collection_Attempts': 0,
    'Collection_Method': 0,
    'Legal_Action_Taken': 0
}

input_data.update(default_values)
input_df = pd.DataFrame([input_data])

# Encode categorical features
for col in input_df.select_dtypes(include="object").columns:
    if col in label_encoders:
        input_df[col] = label_encoders[col].transform(input_df[col])
    else:
        st.warning(f"Missing encoder for column: {col}")
        input_df[col] = 0  # fallback

# Reorder columns to match training
input_df = input_df[expected_features]

# Predict
if st.button("Predict Loan Status"):
    prediction = model_rf.predict(input_df)[0]
    if prediction == 1:
        st.success("✅ Likely to repay the loan on time.")
    else:
        st.error("⚠️ Likely to default or delay repayment.")
