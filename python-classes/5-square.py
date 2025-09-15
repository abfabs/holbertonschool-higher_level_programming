#!/usr/bin/python3
"""Defines a Square class with validated size, area, and printing."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size=0):
        """Initialize a new Square."""
        self.size = size  # use the property for validation

    @property
    def size(self):
        """Retrieve the current size."""
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

    def my_print(self):
        """Print the square with '#' characters; print empty line if size is 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
