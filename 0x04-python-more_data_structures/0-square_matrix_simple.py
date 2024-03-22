#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [i**2 for row in matrix for i in row]
    return new_matrix
