#!/usr/bin/python3
"""Defines a class Square with size validation and area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
