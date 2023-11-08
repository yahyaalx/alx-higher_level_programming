#!/usr/bin/python3
"""this module defines a file writing func"""


def write_file(filename="", text=""):
    """write a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
