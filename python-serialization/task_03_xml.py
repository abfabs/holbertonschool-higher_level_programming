#!/usr/bin/python3
"""
XML Serialization Module

This module provides functions to serialize a Python dictionary
to an XML file and deserialize an XML file back into a dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {child.tag: child.text for child in root}
        return data
    except (ET.ParseError, FileNotFoundError, IOError):
        return {}
