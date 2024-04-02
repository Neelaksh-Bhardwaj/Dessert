# 2024-03-28 23:12:37
import streamlit as st

# Simulated user authentication
def authenticate(username, password):
    return True if username == "admin" and password == "password" else False

# Initialize session state
def initialize_session_state():
    if "user" not in st.session_state:
        st.session_state.user = None
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

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

# Increment a counter to generate unique keys for each button
login_button_counter = 0

def main():
    global login_button_counter
    initialize_session_state()

    st.title("HappieeBitees - Dessert Ordering System")

    # Header layout
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        if st.button("Home"):
            st.write("Welcome to HappieeBitees! Order your favorite desserts here.")
    with col2:
        if st.button("About"):
            st.write("About HappieeBitees: We offer a variety of delicious desserts.")
    with col3:
        if st.button("Login"):
            st.write("### Login")
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")

                # Generate unique key for each "Login" button using the counter
                login_button_counter += 1

                if st.form_submit_button("Login"):
                    if authenticate(username, password):
                        st.success("Login successful!")
                        st.session_state.logged_in = True
                        st.session_state.user = username
                    else:
                        st.error("Invalid credentials")
    with col4:
        if st.button("Contact Us"):
            st.write("Contact us at: contact@happieebitees.com")

    # Display "Menu" section separately
    st.markdown("---")
    st.write("### Menu:")
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
                "Croissant": {"price": 90, "calories": 180, "image": "https://th.bing.com/th/id/OIP.88FcvyyiS8DxuWly8TSmnwHaGe?w=226&h=198&c=7&r=0&o=5&pid=1.7"},
                "Danish Pastry": {"price": 100, "calories": 190, "image": "https://via.placeholder.com/150"},
                "Éclair": {"price": 110, "calories": 200, "image": "https://via.placeholder.com/150"},
                "Cannoli": {"price": 120, "calories": 210, "image": "https://via.placeholder.com/150"},
                "Palmier": {"price": 80, "calories": 170, "image": "https://via.placeholder.com/150"},
            },
        # Other dessert categories...
    }

    selected_category = st.radio("Select a Category", list(dessert_categories.keys()))

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
                    if st.session_state.user in previous_orders:
                        previous_orders[st.session_state.user].append(selected_dessert)
                    else:
                        previous_orders[st.session_state.user] = [selected_dessert]

    st.markdown("---")
    st.write("### Selected Desserts:")
    total_cost = 0
    total_calories = 0
    for order in previous_orders.get(st.session_state.user, []):
        st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")
        total_cost += order['price']
        total_calories += order['calories']

    st.write(f"### Total Cost: ₹{total_cost}")
    st.write(f"### Total Calories: {total_calories}")

    if st.button("Place Order", key="PlaceOrderButton"):
        if len(previous_orders.get(st.session_state.user, [])) == 0:
            st.error("Please select at least one dessert.")
        else:
            st.success("Order placed successfully!")
            st.write("### Order Summary:")
            st.write("#### Selected Desserts:")
            for order in previous_orders[st.session_state.user]:
                st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")
            st.write(f"#### Total Cost: ₹{total_cost}")
            st.write(f"#### Total Calories: {total_calories}")

    # Display Previous Orders
    if st.session_state.get("logged_in"):
        if st.session_state.user in previous_orders:
            st.markdown("---")
            st.write("### Previous Orders:")
            for order in previous_orders[st.session_state.user]:
                st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")

    # Display Dessert Recommendations
    st.markdown("---")
    st.write("### Dessert Recommendations:")
    for dessert, recommendation in dessert_recommendations.items():
        st.write(f"- **{dessert}:** {recommendation}")

if __name__ == "__main__":
    main()
