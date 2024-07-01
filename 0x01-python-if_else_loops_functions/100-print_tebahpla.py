#!/usr/bin/python3
i = 90
while i >= 65:
    if i % 2 == 0:
        print(chr(i + 32), end="")
        i -= 1
    else:
        print(chr(i), end="")
        i -= 1
