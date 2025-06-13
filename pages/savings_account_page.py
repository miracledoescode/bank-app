import streamlit as st

st.set_page_config(page_title="Savings Account", layout="centered")
st.title("My Savings Account")
st.subheader("Balance: N10000")
st.subheader("Limit: N5000")

with st.form("savings_form"):
    amount = st.number_input("Enter amount", min_value=1000)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")