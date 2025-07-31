from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='ecommerce2'
)

@app.route('/api/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        data = request.get_json()
        cursor = conn.cursor()
        insert_query = "INSERT INTO products2 (name, price, description) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (data['name'], data['price'], data['description']))
        conn.commit()
        cursor.close()
        return jsonify({"message": "Product added successfully"}), 201
    
if __name__ == '__main__':
    app.run(debug=True)
    
