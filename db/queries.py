from .main_db import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        is_done INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()
    
def add_product(name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO products (name) VALUES (?)", (name,))
    
    conn.commit()
    conn.close()


def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    
    conn.close()
    return data


def update_product(product_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE products SET is_done=? WHERE id=?",
        (status, product_id)
    )
    
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    
    conn.commit()
    conn.close()