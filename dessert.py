import streamlit as st

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

    st.title("Dessert Ordering System")

    # User Authentication
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

        for category, sub_options in dessert_categories.items():
            st.write(f"## {category}")
            for dessert, details in sub_options.items():
                selected = st.checkbox(f"{dessert} - ₹{details['price']} | {details['calories']} Calories", key=dessert)
                if selected:
                    selected_dessert = {
                        "dessert": dessert,
                        "category": category,
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
        if session_state.user in previous_orders:
            st.markdown("---")
            st.write("### Previous Orders:")
            for order in previous_orders[session_state.user]:
                st.write(f"- {order['dessert']} (₹{order['price']}) | {order['calories']} Calories")

        st.markdown("---")
        st.write("### Dessert Recommendations:")
        for dessert, recommendation in dessert_recommendations.items():
            st.write(f"- **{dessert}:** {recommendation}")

if __name__ == "__main__":
    main()











 





