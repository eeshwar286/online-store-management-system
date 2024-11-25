from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.product_name, products.uom_id, products.price_per_unit, uom.uom_name "
    "FROM online_store.products INNER JOIN online_store.uom ON products.uom_id = uom.uom_id")

    cursor.execute(query)

    response = []
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
        #print(product_id, product_name, uom_id, price_per_unit, uom_name)

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(product_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__=='__main__':
    connection = get_sql_connection()
    # to print all the products as dictionary
    print(get_all_products(connection))

    # to print insert function to insert a new product in the products list
    # print(insert_new_product(connection, {
    #     'product_name': 'cutie orange',
    #     'uom_id': '1',
    #     'price_per_unit': '45.99'
    # }))

    # to print delete function to delete existing product from the product list based on the product_id
    # print(delete_product(connection, 14))
