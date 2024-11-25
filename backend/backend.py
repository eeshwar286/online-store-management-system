import mysql.connector
from flask import jsonify

# Import the SQL connection function
from sql_connection import get_sql_connection


def fetch_all_items():
    connection = get_sql_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM items"
    cursor.execute(query)
    
    items = cursor.fetchall()
    cursor.close()
    return jsonify(items)

def fetch_items_by_search(query):
    connection = get_sql_connection()
    cursor = connection.cursor(dictionary=True)

    query = f"SELECT * FROM items WHERE name LIKE '%{query}%'"
    cursor.execute(query)
    
    items = cursor.fetchall()
    cursor.close()
    return jsonify(items)
