#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    best = 0
    for x in a_dictionary.values():
        if x > best:
            best = x
    return best
