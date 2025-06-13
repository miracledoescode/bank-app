import streamlit as st
from current_account import CurrentAccount

if 'account' not in st.session_state:
    st.session_state.account = CurrentAccount(balance= 10000 )
st.set_page_config(page_title="Current Account", layout="centered")
st.title("Current Account")
st.subheader(f"Balance: N{st.session_state.account.balance}")
with st.form("current_account_form"):
    amount = st.number_input("Enter amount", min_value=1000, step=100)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        try:
            if operations == "Deposit":
                st.session_state.account.deposit(amount)
                st.success(f"Successfuly Depositted N{amount}")
            # add elif statement here for withdraw function

        except ValueError as e:
            st.error(str(e))
