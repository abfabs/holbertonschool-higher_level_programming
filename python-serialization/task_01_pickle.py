#!/usr/bin/python3
"""
Custom Object Serialization using pickle.

This module defines a CustomObject class with the ability to
serialize itself to a file and be deserialized back into an object.
"""

import pickle


class CustomObject:
    """A simple custom object with serialization/deserialization."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file.

        Args:
            filename (str): The name of the file to save the object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Args:
            filename (str): The file containing the serialized object.

        Returns:
            CustomObject or None: The deserialized object, or None if error.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
