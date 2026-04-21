import sqlite3
from config import DB_NAME

def add_product(name, quantity):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()


def get_products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, name, quantity, done FROM products")
    rows = cur.fetchall()
    conn.close()
    return rows


def toggle_done(product_id, value):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE products SET done=? WHERE id=?", (int(value), product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()