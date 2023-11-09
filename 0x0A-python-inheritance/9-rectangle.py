#!/usr/bin/python3
"""the class BaseGeometry and subclass Rectangle"""


class BaseGeometry:
    """public instance methods area and integer_validator"""
    def area(self):
        """raises an excep if called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an in > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A repres of a rectangle"""
    def __init__(self, width, height):
        """init of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
