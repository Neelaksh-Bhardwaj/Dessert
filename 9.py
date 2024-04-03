import streamlit as st
import stripe
import requests
from PIL import Image
import torch
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from food_bot import FoodRecommendationBot  # Assuming FoodRecommendationBot is a class defined in food_bot.py

# Set your Stripe keys
stripe.api_key = "sk_test_51OzGXRSHTYMBDhE84BjlISnZpeBWZsW8AKsEv5mlRQKiVosCDXIkWZPmWXzafYmiTUo3hS33AN0VKfiocbxBcH1Q00g5m8CInA"
publishable_key = "pk_test_51OzGXRSHTYMBDhE8O2MSh7NLKcTp7515CWgHAgYYx3jvtV0gNmn91BoJ3JqmLEMwTygD77DKz9e68xGsEQYkdv1w00bZDu9pwW"

# Background Image
def get_background_image(category):
    response = requests.get(f"https://source.unsplash.com/featured/?{category}")
    return response.url

# Simulated user authentication
def authenticate(username, password):
    return True if username == "admin" and password == "password" else False

# Simulated previous orders for users
previous_orders = {
    "admin": [
        {"dessert": "Cake", "category": "Cakes", "price": 500, "calories": 250},
        {"dessert": "Ice Cream", "category": "Ice Cream", "price": 150, "calories": 120},
    ],
    "user1": [
        {"dessert": "Pie", "category": "Pies", "price": 300, "calories": 180},
        {"dessert": "Cupcake", "category": "Cakes", "price": 100, "calories": 80},
    ]
}

# Simulated dessert recommendations
dessert_recommendations = {
    "Cake": "Try our delicious chocolate cake!",
    "Ice Cream": "Cool down with our creamy ice cream!",
    "Cookie": "Freshly baked cookies, perfect with coffee!",
    "Pie": "Warm apple pie with a scoop of ice cream - a classic!",
    "Brownie": "Indulge in our fudgy brownies!",
    "Cupcake": "Colorful and delightful cupcakes for any occasion!",
    "Cheesecake": "Creamy cheesecake, a slice of heaven!",
    "Pudding": "Rich and comforting pudding, a perfect dessert!"
}

# Define the list of available food categories
food_categories = [
    'burger', 'butter_naan', 'chai', 'chapati', 'chole_bhature', 'dal_makhani',
    'dhokla', 'fried_rice', 'idli', 'jalebi', 'kaathi_rolls', 'kadai_paneer',
    'kulfi', 'masala_dosa', 'momos', 'paani_puri', 'pakode', 'pav_bhaji', 'pizza',
    'samosa'
]

# Load the pre-trained feature extractor and model
feature_extractor = AutoFeatureExtractor.from_pretrained("rajistics/finetuned-indian-food")
model = AutoModelForImageClassification.from_pretrained("rajistics/finetuned-indian-food")

# Define the Streamlit app layout
def main():
    session_state = st.session_state

    st.title("Happieebitees - Sweetness in Every Byte, Hapieebitees' with Sugar-Free Delight.")

    # Display the logo with adjusted size
    logo_image = "https://i.ibb.co/4N8SGmv/Image-20240325-182202-648.png"
    st.image(logo_image, use_column_width=False, width=200)

    # Navigation Bar

    # Title Bar as Scroll Bar
    st.markdown("""
        <style>
            .reportview-container .main .block-container {
                max-width: 100%;
            }
            .reportview-container .main {
                padding-top: 0rem;
            }
            .reportview-container .main .block-container {
                padding-top: 0rem;
                padding-right: 0rem;
                padding-left: 0rem;
            }
            .reportview-container .main .block-container .block-content {
                padding-right: 0rem;
                padding-left: 0rem;
            }
            .reportview-container .main .block-container .block-content p {
                margin-bottom: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header as Navigation Bar
    menu_option = st.selectbox("Menu",
                                ["Home", "About", "Login", "Contact Us"])

    if menu_option == "Home":
        st.write("Welcome to HappieeBitees! Order your favorite desserts here.")
    elif menu_option == "About":
        st.write("About HappieeBitees: We offer a variety of delicious desserts.")
    elif menu_option == "Login":
        st.sidebar.title("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if authenticate(username, password):
                st.sidebar.success("Login successful!")
                session_state.logged_in = True
                session_state.user = username
            else:
                st.sidebar.error("Invalid credentials")

    # Check if the user is logged in before accessing user-specific data
    if session_state.get("logged_in"):
        st.sidebar.subheader(f"Logged in as: {session_state.user}")
        if st.sidebar.button("Logout"):
            session_state.logged_in = False
            session_state.user = None

        # Dessert Categories with Sub-options
        dessert_categories = {
            "Cakes": {
                "Chocolate Cake": {"price": 500, "calories": 300},
                "Vanilla Cake": {"price": 450, "calories": 280},
                "Strawberry Shortcake": {"price": 550, "calories": 320},
                "Red Velvet Cake": {"price": 520, "calories": 310},
                "Carrot Cake": {"price": 480, "calories": 290},
            },
            "Shakes": {
                "Chocolate Shake": {"price": 150, "calories": 200},
                "Vanilla Shake": {"price": 130, "calories": 180},
                "Strawberry Shake": {"price": 160, "calories": 220},
                "Banana Shake": {"price": 140, "calories": 190},
                "Caramel Shake": {"price": 170, "calories": 240},
            },
            "Coffee": {
                "Espresso": {"price": 80, "calories": 5},
                "Cappuccino": {"price": 120, "calories": 80},
                "Latte": {"price": 100, "calories": 60},
                "Mocha": {"price": 130, "calories": 90},
                "Americano": {"price": 90, "calories": 10},
            },
            "Brownies": {
                "Classic Brownie": {"price": 100, "calories": 200},
                "Walnut Brownie": {"price": 120, "calories": 220},
                "Blondie": {"price": 110, "calories": 210},
                "Fudge Brownie": {"price": 130, "calories": 230},
                "Peanut Butter Brownie": {"price": 140, "calories": 240},
            },
            "Pastries": {
                "Croissant": {"price": 90, "calories": 180},
                "Danish Pastry": {"price": 100, "calories": 190},
                "Éclair": {"price": 110, "calories": 200},
                "Cannoli": {"price": 120, "calories": 210},
                "Palmier": {"price": 80, "calories": 170},
            }
        }

        st.markdown("---")
        st.write("### Menu:")
        st.markdown("---")

        selected_category = st.sidebar.selectbox("Select a Category", list(dessert_categories.keys()))

        if selected_category:
            st.write(f"## {selected_category}")
            for dessert, details in dessert_categories[selected_category].items():
                col1, col2 = st.columns([1, 3])
                with col1:
                    background_image = get_background_image(selected_category)
                    st.image(background_image, use_column_width=True)
                with col2:
                    selected = st.checkbox(f"{dessert} - ₹{details['price']} | {details['calories']} Calories", key=dessert)
                    if selected:
                        selected_dessert = {
                            "dessert": dessert,
                            "category": selected_category,
                            "price": details['price'],
                            "calories": details['calories']
                        }
                        if session_state.user in previous_orders:
                            previous_orders[session_state.user].append(selected_dessert)
                        else:
                            previous_orders[session_state.user] = [selected_dessert]

        st.markdown("---")
        st.write("### Selected Desserts:")
        total_cost = 0
        total_calories = 0
        for order in previous_orders.get(session_state.user, []):
            st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")
            total_cost += order['price']
            total_calories += order['calories']

        st.write(f"### Total Cost: ₹{total_cost}")
        st.write(f"### Total Calories: {total_calories}")

        if st.button("Place Order"):
            if len(previous_orders.get(session_state.user, [])) == 0:
                st.error("Please select at least one dessert.")
            else:
                st.success("Order placed successfully!")
                st.write("### Order Summary:")
                st.write("#### Selected Desserts:")
                for order in previous_orders[session_state.user]:
                    st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")
                st.write(f"#### Total Cost: ₹{total_cost}")
                st.write(f"#### Total Calories: {total_calories}")

                # Render the Stripe Checkout form
                st.write("## Place Order")
                product_name = "Desserts"
                price = total_cost  # Updated price to total_cost

                # Add currency selection option
                currency = "INR"  # Default to INR for simplicity

                if currency == "INR":
                    unit_amount = int(price*100)  # Stripe expects amount in lowest currency unit (e.g., paise for INR)
                else:
                    unit_amount = int(price*100)  # Stripe expects amount in cents for USD

                session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[{
                        "price_data": {
                            "currency": currency.lower(),
                            "product_data": {
                                "name": product_name,
                            },
                            "unit_amount": unit_amount,
                        },
                        "quantity": 1,
                    }],
                    mode="payment",
                    success_url="https://your-streamlit-app.com/success",
                    cancel_url="https://your-streamlit-app.com/cancel",
                )

                st.write(f"Please visit: {session.url} to complete the payment.")

    # Display Previous Orders
    if session_state.get("logged_in"):
        if session_state.user in previous_orders:
            st.markdown("---")
            st.write("### Previous Orders:")
            for order in previous_orders[session_state.user]:
                st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")

    # Display Dessert Recommendations
    st.markdown("---")
    st.write("### Dessert Recommendations:")
    for dessert, recommendation in dessert_recommendations.items():
        st.write(f"- **{dessert}:** {recommendation}")

    # Indian Food Image Classification
    st.markdown("---")
    st.title("Indian Food Image Classification")
    st.markdown("Upload an image to classify it into different Indian food categories.")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Prepare the image for the model
        encoding = feature_extractor(image.convert("RGB"), return_tensors="pt")

        # Perform inference
        with torch.no_grad():
            outputs = model(**encoding)
            logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_class = model.config.id2label[predicted_class_idx]

        # Display the prediction
        st.success(f"Predicted class: {predicted_class}")

    # Dropdown to select food category
    selected_category = st.selectbox('These categories are available ', food_categories)
    st.write('You selected:', selected_category)

        # Food Recommendation Bot
    st.markdown("---")
    st.title("Food Recommendation Bot")
    api_key = 'b8e473f0c34d4f858e1785a7bd4d1126'  # Replace with your actual API key
    user_input = st.text_input("Enter your food preference:")
    if st.button("Get Recommendations"):
        bot = FoodRecommendationBot(api_key)  # Instantiate the FoodRecommendationBot object
        recommendations = bot.get_recommendations(user_input)
        if recommendations:
            st.write("Here are some recommendations:")
            for idx, title in enumerate(recommendations, 1):
                st.write(f"{idx}. {title}")
        else:
            st.write("Sorry, no recommendations found.")

if __name__ == "__main__":
    main()