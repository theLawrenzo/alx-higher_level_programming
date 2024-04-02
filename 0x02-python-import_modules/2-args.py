#!/usr/bin/python3
from sys import argv as argv
def print_args(argv):
    length = len(argv)
    count = count + 1
    if lenght == 0:
        print("0 arguments.")
    for i in argv:
        if lenght == 1:
            print("1 argument:")
            print("{:d}. {:s}".format(count, i))
            return None
        print("{:d} arguments:".format(length))
        print("{:d}. {:s}".format(count, i))
        count = count + i
