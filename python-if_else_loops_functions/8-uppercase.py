#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    out = ""
    for ch in str:
        code = ord(ch)
        if 97 <= code <= 122:
            code -= 32
        out += chr(code)
    print("{}".format(out))
