import streamlit as st

# Simulated user authentication
def authenticate(username, password):
    return True if username == "admin" and password == "password" else False

# Simulated previous orders for users
previous_orders = {
    "admin": [
        {"dessert": "Cake", "cost": 20.00},
        {"dessert": "Ice Cream", "cost": 5.00},
    ],
    "user1": [
        {"dessert": "Pie", "cost": 15.00},
        {"dessert": "Cupcake", "cost": 3.00},
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

        # Dessert Ordering
        dessert_options = {
            "Cake": 20.00,
            "Ice Cream": 5.00,
            "Cookie": 2.50,
            "Pie": 15.00,
            "Brownie": 4.00,
            "Cupcake": 3.00,
            "Cheesecake": 18.00,
            "Pudding": 6.50
        }

        selected_desserts = []
        total_cost = 0.0

        st.markdown("---")
        st.write("### Menu:")
        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            for dessert, price in list(dessert_options.items())[:len(dessert_options)//2]:
                if st.checkbox(f"{dessert} - ${price}", key=dessert):
                    selected_desserts.append({"dessert": dessert, "cost": price})
                    total_cost += price

        with col2:
            for dessert, price in list(dessert_options.items())[len(dessert_options)//2:]:
                if st.checkbox(f"{dessert} - ${price}", key=dessert):
                    selected_desserts.append({"dessert": dessert, "cost": price})
                    total_cost += price

        st.markdown("---")
        st.write("### Selected Desserts:")
        for dessert in selected_desserts:
            st.write(f"- {dessert['dessert']} (${dessert['cost']:.2f})")

        st.write(f"### Total Cost: ${total_cost:.2f}")

        if st.button("Place Order"):
            if len(selected_desserts) == 0:
                st.error("Please select at least one dessert.")
            else:
                if session_state.user in previous_orders:
                    previous_orders[session_state.user].extend(selected_desserts)
                else:
                    previous_orders[session_state.user] = selected_desserts

                st.success("Order placed successfully!")
                st.write("### Order Summary:")
                st.write("#### Selected Desserts:")
                for dessert in selected_desserts:
                    st.write(f"- {dessert['dessert']} (${dessert['cost']:.2f})")
                st.write(f"#### Total Cost: ${total_cost:.2f}")

        # Display Previous Orders
        if session_state.user in previous_orders:
            st.markdown("---")
            st.write("### Previous Orders:")
            for order in previous_orders[session_state.user]:
                st.write(f"- {order['dessert']} (${order['cost']:.2f})")

        # Display Dessert Recommendations
        st.markdown("---")
        st.write("### Dessert Recommendations:")
        for dessert, recommendation in dessert_recommendations.items():
            st.write(f"- **{dessert}:** {recommendation}")

if __name__ == "__main__":
    main()
