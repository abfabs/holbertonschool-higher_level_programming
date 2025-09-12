#!/usr/bin/env python3

def add_integer(a, b=98):
    """Add two integers or floats, converting to int before addition.

    Args:
        a: First number to add.
        b: Second number to add (defaults to 98).

    Returns:
        int: Sum of a and b after conversion to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
