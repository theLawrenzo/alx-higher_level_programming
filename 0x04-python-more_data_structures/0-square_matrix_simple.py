#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if len(matrix) != 0:
        for m in matrix:
            new_matrix.append([i ** 2 for i in m])

    return new_matrix
