#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = list(dict.keys(a_dictionary))
    list_keys.sort()
    j = 0

    for i in a_dictionary:
        print("%s: %s" %(list_keys[j], a_dictionary[list_keys[j]]))
        j = j + 1
    
    return None
