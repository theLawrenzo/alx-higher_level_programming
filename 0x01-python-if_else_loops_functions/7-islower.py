#!/usr/bin/python3
def islower(c):
    ch = ord(c)
    if ch >= 90 and ch <= 65:
        return False
    elif ch >= 97 and ch <= 122:
        return True
