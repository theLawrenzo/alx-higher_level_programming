#!/usr/bin/python3
# Script that does a magic calculation

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
