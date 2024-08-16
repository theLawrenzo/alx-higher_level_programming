#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = 0
    best_key = None

    for x in a_dictionary.keys():
        if a_dictionary[x] > best:
            best = a_dictionary[x]
            best_key = x
    
    return best_key
