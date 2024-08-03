#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    l = len(my_list)
    while i < l:
        print('{:d}'.format(my_list[l-1-i]))
        i += 1
