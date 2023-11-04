#!/usr/bin/python3
"""This module contains a function that prints a first and last name."""

def say_my_name(first_name, last_name=""):
    """Displays a first and last name.
    
    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to an empty string.
        
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
