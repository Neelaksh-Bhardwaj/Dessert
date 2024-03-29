import streamlit as st

# Set theme colors
PRIMARY_COLOR = "#9B30FF"  # Purple
SECONDARY_COLOR = "#FF69B4"  # Pink
BACKGROUND_COLOR = "#FFB6C1" # Pink background

# Custom CSS
st.markdown(
    f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
        }}
        .sidebar .sidebar-content {{
            background-color: {PRIMARY_COLOR};
            color: white;
        }}
        .sidebar .sidebar-content .stButton {{
            color: black;
        }}
        .sidebar .sidebar-content .stTextInput > div > div > input {{
            color: black;
        }}
        .stButton {{
            background-color: {SECONDARY_COLOR};
            color: white;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

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

def main():
    session_state = st.session_state

    st.title("HappieeBitees - Dessert Ordering System")

    # Navigation Bar
    menu_option = st.sidebar.selectbox("Menu",
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
                "Chocolate Cake": {"price": 500, "calories": 300, "image": "https://via.placeholder.com/150"},
                "Vanilla Cake": {"price": 450, "calories": 280, "image": "https://via.placeholder.com/150"},
                "Strawberry Shortcake": {"price": 550, "calories": 320, "image": "https://via.placeholder.com/150"},
                "Red Velvet Cake": {"price": 520, "calories": 310, "image": "https://via.placeholder.com/150"},
                "Carrot Cake": {"price": 480, "calories": 290, "image": "https://via.placeholder.com/150"},
            },
            "Shakes": {
                "Chocolate Shake": {"price": 150, "calories": 200, "image": "https://via.placeholder.com/150"},
                "Vanilla Shake": {"price": 130, "calories": 180, "image": "https://via.placeholder.com/150"},
                "Strawberry Shake": {"price": 160, "calories": 220, "image": "https://via.placeholder.com/150"},
                "Banana Shake": {"price": 140, "calories": 190, "image": "https://via.placeholder.com/150"},
                "Caramel Shake": {"price": 170, "calories": 240, "image": "https://via.placeholder.com/150"},
            },
            "Coffee": {
                "Espresso": {"price": 80, "calories": 5, "image": "https://via.placeholder.com/150"},
                "Cappuccino": {"price": 120, "calories": 80, "image": "https://via.placeholder.com/150"},
                "Latte": {"price": 100, "calories": 60, "image": "https://via.placeholder.com/150"},
                "Mocha": {"price": 130, "calories": 90, "image": "https://via.placeholder.com/150"},
                "Americano": {"price": 90, "calories": 10, "image": "https://via.placeholder.com/150"},
            },
            "Brownies": {
                "Classic Brownie": {"price": 100, "calories": 200, "image": "https://via.placeholder.com/150"},
                "Walnut Brownie": {"price": 120, "calories": 220, "image": "https://via.placeholder.com/150"},
                "Blondie": {"price": 110, "calories": 210, "image": "https://via.placeholder.com/150"},
                "Fudge Brownie": {"price": 130, "calories": 230, "image": "https://via.placeholder.com/150"},
                "Peanut Butter Brownie": {"price": 140, "calories": 240, "image": "https://via.placeholder.com/150"},
            },
            "Pastries": {
                "Croissant": {"price": 90, "calories": 180, "image": "https://via.placeholder.com/150"},
                "Danish Pastry": {"price": 100, "calories": 190, "image": "https://via.placeholder.com/150"},
                "Éclair": {"price": 110, "calories": 200, "image": "https://via.placeholder.com/150"},
                "Cannoli": {"price": 120, "calories": 210, "image": "https://via.placeholder.com/150"},
                "Palmier": {"price": 80, "calories": 170, "image": "https://via.placeholder.com/150"},
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
                    image = details.get('image', 'https://via.placeholder.com/150')
                    st.image(image, use_column_width=True)
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

if __name__ == "__main__":
    main()
