import streamlit as st

st.set_page_config(page_title="Bank App", layout="centered")

st.title("🏦 Welcome to Your Bank")
st.subheader("Choose an account type to proceed with")

st.page_link(page="pages/current_account_page.py", label="Current account →", icon="💼", use_container_width=100)
st.page_link(page="pages/savings_account_page.py", label="Savings account →", icon="💰", use_container_width=100)