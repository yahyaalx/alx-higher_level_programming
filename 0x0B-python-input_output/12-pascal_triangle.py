#!/usr/bin/python3
"""Defines a Pascal triangle func"""

def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal's triangle of n """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        last_row = pascal[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        pascal.append(new_row)
    return pascal
