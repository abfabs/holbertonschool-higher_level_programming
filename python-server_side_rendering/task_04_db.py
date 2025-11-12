#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_file(filename):
    products = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
    except FileNotFoundError:
        pass
    return products

def read_sqlite_db(filename):
    """Reads data from SQLite database"""
    products = []
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except sqlite3.Error:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error_message = None
    products_data = []

    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')
    elif source == 'sql':
        products_data = read_sqlite_db('products.db')
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    if product_id is not None:
        products_data = [p for p in products_data if p.get('id') == product_id]
        if not products_data:
            error_message = "Product not found"

    return render_template('product_display.html', products=products_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
