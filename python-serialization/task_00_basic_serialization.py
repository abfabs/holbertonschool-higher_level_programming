#!/usr/bin/python3
"""
Basic Serialization Module

This module provides functions to:
- Serialize and save a Python dictionary to a JSON file.
- Load and deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file where the JSON will be stored.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
