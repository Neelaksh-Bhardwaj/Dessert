import streamlit as st
from passlib.hash import pbkdf2_sha256
import time

# Create a dictionary of users (for demonstration purposes)
users = {
    "user1": {
        "password": pbkdf2_sha256.hash("password1"),
        "favorite_dessert": "Cheesecake"
    },
    "user2": {
        "password": pbkdf2_sha256.hash("password2"),
        "favorite_dessert": "Chocolate Cake"
    }
}

# Color schemes
PRIMARY_COLOR = "#FF5733"
SECONDARY_COLOR = "#FFE8D6"
TEXT_COLOR = "#333333"

# Custom CSS for styling
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {SECONDARY_COLOR};
            background-image: url('https://i.ibb.co/zmjh0dZ/IMG-0459.jpg');
            background-size: cover;
            background-position: center;
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: white;
        }}
        .stTextInput>div>div>input {{
            color: {TEXT_COLOR};
        }}
        .animated-logo {{
            animation: bounce 2s infinite alternate;
        }}
        @keyframes bounce {{
            from {{ transform: translateY(0); }}
            to {{ transform: translateY(-10px); }}
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Animated dessert image
dessert_image = """
    <img src="https://i.imgur.com/5WLqTTF.gif" class="animated-logo" width="200" height="200">
"""

def login():
    st.markdown("<h1 style='text-align: center; color: #FF5733;'> Dessert Recommendation and Ordering </h1>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        with st.spinner("Logging in..."):
            time.sleep(2)  # Simulate server-side processing time
            if username in users and pbkdf2_sha256.verify(password, users[username]["password"]):
                st.success(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Invalid username or password")

def main():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login()
    else:
        st.markdown(dessert_image, unsafe_allow_html=True)
        st.write(f"Welcome back, {st.session_state.username}!")

if __name__ == "__main__":
    main()
