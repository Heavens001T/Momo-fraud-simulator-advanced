import streamlit as st
from model import train_model, predict_transaction
from data_generator import generate_transaction
from utils import risk_decision, calculate_weighted_risk
import pandas as pd

st.set_page_config(page_title="AI Mobile Money Fraud Simulator", layout="wide")
st.title("📱 Advanced Mobile Money Fraud Simulator")
st.sidebar.header("Transaction Simulation Options")

# Train AI
model, columns = train_model()

# Mode selection
mode = st.sidebar.radio("Mode", ["Manual Input", "Random Transaction"])

if mode == "Manual Input":
    amount = st.sidebar.slider("Amount (FCFA)", 500, 500_000, 5000)
    hour = st.sidebar.slider("Hour", 0,23,12)
    tx_count = st.sidebar.slider("Transactions in Last Hour",1,20,1)
    new_device = st.sidebar.selectbox("New Device?", ["No","Yes"])
    location = st.sidebar.selectbox("Location", ["Yaoundé","Douala","Bamenda","Garoua","Limbe"])
    tx_type = st.sidebar.selectbox("Transaction Type", ["Send Money","Pay Bill","Airtime Top-Up","Withdraw Cash"])
    user_profile = st.sidebar.selectbox("User Profile", ["Normal","VIP","Agent"])
    new_device_val = 1 if new_device=="Yes" else 0
    tx = pd.DataFrame([{
        "amount": amount,
        "hour": hour,
        "transactions_last_hour": tx_count,
        "new_device": new_device_val,
        "location": location,
        "tx_type": tx_type,
        "user_profile": user_profile
    }])
else:
    tx = generate_transaction()

# Predict AI fraud
prediction, probability = predict_transaction(model, tx)
weighted_risk = calculate_weighted_risk(tx)
decision, level = risk_decision(probability)

# Show result
st.subheader("🧠 AI Fraud Decision")
st.write(f"**Predicted Fraud Risk:** {round(probability*100,2)}%")
st.write(f"**Weighted Risk Score:** {round(weighted_risk*100,2)}%")

if level=="success":
    st.success(f"✅ Transaction Approved")
elif level=="warning":
    st.warning(f"⚠️ OTP Verification Required")
else:
    st.error(f"❌ Transaction Blocked")

# Transaction log
if "log" not in st.session_state:
    st.session_state["log"] = tx.copy()
else:
    st.session_state["log"] = st.session_state["log"].append(tx, ignore_index=True)

st.subheader("📊 Transaction Log")
st.dataframe(st.session_state["log"])
