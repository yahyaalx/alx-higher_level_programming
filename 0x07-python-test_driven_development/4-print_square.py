#!/usr/bin/python3
"""This module contains a function that prints a square using the '#' character."""

def print_square(size):
    """Prints a square of a given size using the '#' character.
    
    Args:
        size (int): The size of the square to be printed.
        
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
