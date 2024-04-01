import streamlit as st
import stripe

# Set your Stripe keys
stripe.api_key = "sk_test_51OzGXRSHTYMBDhE84BjlISnZpeBWZsW8AKsEv5mlRQKiVosCDXIkWZPmWXzafYmiTUo3hS33AN0VKfiocbxBcH1Q00g5m8CInA"
publishable_key = "pk_test_51OzGXRSHTYMBDhE8O2MSh7NLKcTp7515CWgHAgYYx3jvtV0gNmn91BoJ3JqmLEMwTygD77DKz9e68xGsEQYkdv1w00bZDu9pwW"

# Render the Stripe Checkout form
st.write("## Buy Product")
product_name = st.text_input("Product Name")
price = st.number_input("Price (INR)")

# Add currency selection option
currency = st.selectbox("Currency", ["INR", "USD"])

if st.button("Buy"):
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
