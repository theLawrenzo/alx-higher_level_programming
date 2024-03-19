#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    length = len(my_list)
    if idx > length:
        return my_list
    new = []
    for i in my_list:
        new.append(i)
    new[idx] = element
    return new
