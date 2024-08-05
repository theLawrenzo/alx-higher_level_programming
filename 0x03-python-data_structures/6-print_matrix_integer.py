#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            if j == len(row) - 1:
                print('{:d}'.format(j), end="")
            else:
                print('{:d}'.format(j), end=" ")
            j += 1
        print()
        i += 1
