#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    """Reads products from JSON file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_file(filename):
    """Reads products from CSV file"""
    products = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields properly
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
    except FileNotFoundError:
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
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # Filter by id if provided
    if product_id is not None:
        products_data = [p for p in products_data if p.get('id') == product_id]
        if not products_data:
            error_message = "Product not found"

    return render_template('product_display.html', products=products_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
