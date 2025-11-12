#!/usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # Read data from JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except FileNotFoundError:
        items_list = []

    # Render the template with items
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)
