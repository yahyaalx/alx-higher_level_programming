#!/usr/bin/python3
""" a class that def a rec"""
class Rectangle:
    """
    This class defines a rectangle and provides width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of the Rectangle class.
        
        Args:
            width (int): Represents the width of the rectangle. Default is 0.
            height (int): Represents the height of the rectangle. Default is 0.
        
        Raises:
            TypeError: If width or height is not of integer type.
            ValueError: If width or height is less than zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width attribute.

        Args:
            value (int): The value to set as the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height attribute.

        Args:
            value (int): The value to set as the height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
