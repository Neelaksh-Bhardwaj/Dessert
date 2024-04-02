import streamlit as st
from authentication import authenticate

def show_login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
