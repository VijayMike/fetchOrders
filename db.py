import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    item TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
cursor.executemany(
    "INSERT INTO orders (customer_name, item, quantity, price) VALUES (?, ?, ?, ?)",
    [
        ("Mike", "Laptop", 1, 200000),
        ("Sush", "Smartphone", 2, 114000),
        ("Vijay", "Headphones", 3, 25000),
    ]
)

conn.commit()
conn.close()
