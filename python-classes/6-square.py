#!/usr/bin/python3
"""Defines a Square class with size, position, area, and printing."""


class Square:
    """Represents a square with a private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with optional size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the current position (x, y) offset."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position ensuring it is a tuple of 2 non-negative integers."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' using position as an offset.

        If size is 0, prints an empty line.
        Vertical offset is added as leading newlines (no spaces on those lines).
        Horizontal offset is added as leading spaces on each printed row.
        """
        if self.__size == 0:
            print()
            return

        # Vertical offset
        print("\n" * self.__position[1], end="")

        # Draw each row with horizontal offset then hashes
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
