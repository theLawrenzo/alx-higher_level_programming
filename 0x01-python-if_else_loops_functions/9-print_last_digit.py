#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        i = 0
        while number < 0:
            i = i+1
            number = number+1
        number = i
    ld = number % 10
    print("{}".format(ld), end="")
    return ld
