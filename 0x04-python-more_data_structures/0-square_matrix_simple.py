#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_matrix = [[col * col for col in row] for row in matrix]
    return new_matrix
