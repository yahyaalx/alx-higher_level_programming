#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""
    def __eq__(self, num):
        """for =="""
        return (int(self) != int(num))

    def __ne__(self, num):
        """for !="""
        return (int(self) == int(num))
