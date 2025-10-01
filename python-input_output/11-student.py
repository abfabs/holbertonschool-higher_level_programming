#!/usr/bin/python3
"""
This module defines the Student class.
It provides a simple implementation of serialization and
deserialization (object to dictionary and back).
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes
        are retrieved.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys are attribute names
                         and values are the new values to assign.
        """
        for key, value in json.items():
            setattr(self, key, value)
