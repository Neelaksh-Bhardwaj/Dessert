import streamlit as st
from food_bot import FoodRecommendationBot
import requests
api_key = 'b8e473f0c34d4f858e1785a7bd4d1126'  # Replace with your actual API key
bot = FoodRecommendationBot(api_key)
st.title("Food Recommendation Bot")
user_input = st.text_input("Enter your food preference:")
if st.button("Get Recommendations"):
    recommendations = bot.get_recommendations(user_input)
    if recommendations:
        st.write("Here are some recommendations:")
        for idx, title in enumerate(recommendations, 1):
            st.write(f"{idx}. {title}")
    else:
        st.write("Sorry, no recommendations found.")
