import streamlit as st
from savings_account import SavingsAccount
from account import Account


def main():
    st.set_page_config(page_title="Savings Account", layout="centered")
    st.title("🏦 Savings Account overview")
    choice = st.selectbox("Do you want to", ["Deposit", "Withdraw"])
    name = st.text_input("Enter Account Holder Name", "")
    amount = st.number_input("Enter amount", min_value=0, step=100)
    st.subheader(f"Welcome, {name}")

    # Initialize account in session state
    if "account" not in st.session_state or st.session_state.get("account_name") != name:
        st.session_state.account = SavingsAccount(0,5000)
        st.session_state.account_name = name

    account = st.session_state.account
    
    balance_placeholder = st.empty()
    balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")
    
    if st.button("Submit Transactions"):
        if choice == "Deposit":
            account.deposit(amount)
            st.success(f"Deposited ${amount:.2f} in your account")
        elif choice == "Withdraw":
            success = account.withdraw(amount)
            if success:
                st.success(f"Withdrew ${amount:.2f} from your account")
            else:
                # Only SavingsAccount is supported here, so show withdrawal limit error
                st.error(f"❌ Withdrawal failed: Max ${getattr(account, 'withdrawal_limit', 'N/A')} or insufficient balance.")

if __name__ == "__main__":
    main()
