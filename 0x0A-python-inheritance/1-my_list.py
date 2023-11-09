#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """ Mylist class that inherist from list """

    def print_sorted(self):
        """func that prints a sorted list """
        print(sorted(self))