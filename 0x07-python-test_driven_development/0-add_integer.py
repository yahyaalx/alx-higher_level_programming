#!/usr/bin/python3
"""
This module contains a function that adds two numbers.
"""

def add_integer(a, b=98):
    """
    Function that adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers, after they have been converted to integers.

    Raises:
        TypeError: If 'a' is not an integer or float, it raises "a must be an integer".
        TypeError: If 'b' is not an integer or float, it raises "b must be an integer".
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
