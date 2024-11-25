from flask import Flask, request, jsonify
from flask_cors import CORS
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

connection = get_sql_connection()

# Get all products
@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Add a new product
@app.route('/addProduct', methods=['POST'])
def add_product():
    product = {
        'product_name': request.form['product_name'],
        'uom_id': request.form['uom_id'],
        'price_per_unit': request.form['price_per_unit']
    }
    product_id = products_dao.insert_new_product(connection, product)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Delete a product
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    product_id = request.form['product_id']
    products_dao.delete_product(connection, product_id)
    response = jsonify({
        'message': 'Product deleted successfully',
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for the online store")
    app.run(port=5000)
