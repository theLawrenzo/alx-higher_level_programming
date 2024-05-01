#!/usr/bin/python3
def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a = b
        b = a+b
        print()


def fib2(n):
    res = []
    a = 0
    b = 1
    while a < n:
        res.append(a)
        a = b
        b = a+b
    return res
