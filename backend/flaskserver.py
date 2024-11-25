from flask import Flask, request, render_template
from backend import fetch_all_items, fetch_items_by_search
import mysql.connector

# Initialize Flask application
app = Flask(__name__)

# MySQL connection function
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='kanna123',
                                host='127.0.0.1',
                                database='online_store')
    return __cnx

# Route to fetch all items or search items by query
@app.route('/items', methods=['GET'])
def get_items():
    search_query = request.args.get('search')
    if search_query:
        return fetch_items_by_search(search_query)
    return fetch_all_items()

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
