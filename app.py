import streamlit as st
import requests

st.title("Order List")

url = "http://127.0.0.1:8000/orders"

try:
    response = requests.get(url)
    if response.status_code == 200:
        orders = response.json().get("orders", [])
        if orders:
            st.table(orders)
        else:
            st.write("No orders found.")
    else:
        st.write("Failed to fetch orders.")
except requests.exceptions.ConnectionError:
    st.write("Could not connect to FastAPI server.")
