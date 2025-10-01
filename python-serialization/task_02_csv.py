#!/usr/bin/python3
"""
CSV to JSON Converter Module.

This module provides a function to read data from a CSV file,
convert it into a list of dictionaries, and serialize it to
a JSON file named 'data.json'.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and save it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
