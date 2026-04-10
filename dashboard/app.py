import streamlit as st

st.title("💳 Financial Fraud Detection System")

transaction_id = st.number_input("Transaction ID", value=2001)
customer_id = st.number_input("Customer ID", value=900)
amount = st.number_input("Amount", value=15000)
location = st.number_input("Location Code", value=3)
device = st.number_input("Device Code", value=2)
hour = st.number_input("Hour (0-23)", value=2)
is_night = st.number_input("Is Night (0 or 1)", value=1)

if st.button("Check Fraud"):
    
    if amount > 10000:
        st.error("🚨 Fraud Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")