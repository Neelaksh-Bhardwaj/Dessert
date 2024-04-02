import streamlit as st
from login_page import show_login_page
from home_page import show_home_page
from about_page import show_about_page

def main():
    page = st.sidebar.selectbox("Menu", ["Home", "About", "Login"])
    if page == "Home":
        show_home_page()
    elif page == "About":
        show_about_page()
    elif page == "Login":
        show_login_page()

if __name__ == "__main__":
    main()
