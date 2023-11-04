#!/usr/bin/python3

"""This module contains a function for matrix division."""

def matrix_divided(matrix, div):
    """Performs element-wise division on a matrix.

    Args:
        matrix (list): A nested list of integers or floats.
        div (int/float): The number by which to divide the matrix elements.
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If the matrix rows are not all the same length.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix with the result of the division operation.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
