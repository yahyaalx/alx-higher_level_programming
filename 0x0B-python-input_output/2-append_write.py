#!/usr/bin/python3

"""this module defines a file appending func"""


def append_write(filename="", text=""):
    """appends a string to end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
