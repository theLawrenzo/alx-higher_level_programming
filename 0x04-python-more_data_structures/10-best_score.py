#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and a_dictionary.__len__():
        best = 0
        best_key = None

        for key in a_dictionary.keys():
            if a_dictionary[key] > best:
                best = a_dictionary[key]
                best_key = key
        return best_key
    return None
