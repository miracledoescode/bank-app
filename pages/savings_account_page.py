import streamlit as st

st.set_page_config(page_title="Savings Account", layout="centered")
st.title("My Savings Account")
st.subheader("Balance: ₦10000")
st.subheader("Limit: ₦5000")

if submit:
    try:
        if operations == "Deposit":
            st.success(f"Deposit of ₦{amount} successful!✅")
        elif operations == "Withdraw":
            if amount > 5000:  # Assuming limit is 5000
                st.error("Error: Withdrawal exceeds limit")
            else:
                st.success(f"Withdrawal of ₦{amount} successful!✅")
    except ValueError as e:
        st.error(f"An error occurred: {e}")

with st.form("savings_form"):
    amount = st.number_input("Enter amount", min_value=1000)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")