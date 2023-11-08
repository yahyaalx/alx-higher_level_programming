#!/usr/bin/python3
"""def a python class to JSON func"""


def class_to_json(obj):
    """return the dictionary rep of data struct"""
    return obj.__dict__
