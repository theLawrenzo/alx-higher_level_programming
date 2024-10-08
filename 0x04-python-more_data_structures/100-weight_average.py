#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list) and len(my_list):
        score = 0
        weight = 0
        for x in my_list:
            score += (x[0] * x[1])
            weight += (x[1])
        return (score / weight)
    return 0
