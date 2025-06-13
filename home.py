import streamlit as st
from savings_acccount import SavingsAccount
st.set_page_config(page_title="Bank App", layout="centered")
savings = SavingsAccount(20000)

with st.form("savings_form"):
    amount = st.number_input("Enter Amount to save", min_value=1000)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")
    if submit and operations == "Withdraw":
        with st.spinner("Processing..."):
            savings.withdraw(amount)
            print(savings.balance)