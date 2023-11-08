#!/usr/bin/python3
"""defines a class Studentand init it"""


class Student:
    """representation of a student"""

    def __init__(self, first_name, last_name, age):
        """init a new Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list and all([type(s) == str for s in attrs]):
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__
    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
    items = list(json.items())
    i = 0
    while i < len(items):
        key, value = items[i]
        self.__dict__[key] = value
        i += 1
