#!/usr/bin/python3
def best_score(a_dictionary):
    if len(list(a_dictionary)) == 0:
        return None

    scores_keys = list(a_dictionary.keys())
    first = scores_keys[0]
    best_score_key = first
    best_score = a_dictionary[first]

    for key in a_dictionary:
        if a_dictionary[key] > best_score:
            best_score = a_dictionary[key]
            best_score_key = key

    return best_score_key
