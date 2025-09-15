#!/usr/bin/python3
"""Defines a Square class with validated size and area computation."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size  # route through the property for validation

    @property
    def size(self):
        """Get the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with type/value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
