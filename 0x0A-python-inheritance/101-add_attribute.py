#!/usr/bin/python3
"""function that adds attribute to obj"""


def add_attribute(obj, att, value):
    """adds a new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
