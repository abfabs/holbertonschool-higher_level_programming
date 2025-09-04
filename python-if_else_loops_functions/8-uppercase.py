#!/usr/bin/python3
def uppercase(str):
    out = ""
    for ch in str:
        code = ord(ch)
        if 97 <= code <= 122:
            code -= 32
        out += chr(code)
    print("{}".format(out))
