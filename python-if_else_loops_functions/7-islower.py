#!/usr/bin/python3
def islower(c):
    """Return True if c is a lowercase ASCII letter, else False."""
    code = ord(c)
    return 97 <= code <= 122
