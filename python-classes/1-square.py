#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: Size of the square (no type/value verification).
        """
        self.__size = size
