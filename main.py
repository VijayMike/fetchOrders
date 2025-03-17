from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_orders():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, customer_name, item, quantity, price FROM orders")
    orders = [{"id": row[0], "customer_name": row[1], "item": row[2], "quantity": row[3], "price": row[4]} for row in cursor.fetchall()]
    conn.close()
    return orders

@app.get("/orders")
def list_orders():
    return {"orders": get_orders()}
