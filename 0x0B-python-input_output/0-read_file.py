#!/usr/bin/python3
"""module defines a text file reading func"""


def read_file(filename=""):
    """print the content of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
