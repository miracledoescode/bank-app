import streamlit as st

st.set_page_config(page_title="Bank App", layout="centered")

st.page_link(page="pages/current_account_page.py", label="Current account", icon=None, help=None, disabled=False, use_container_width=None)
st.page_link(page="pages/savings_account_page.py", label="Savings account", icon=None, help=None, disabled=False, use_container_width=None)