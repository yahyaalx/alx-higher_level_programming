#!/usr/bin/python3
"""defines a class Studentand init it"""


class Student:
    """representation of a student"""

    def __init__(self, first_name, last_name, age):
        """init a new Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
