#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """return true if obj is subclass of a_class else false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
