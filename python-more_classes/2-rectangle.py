#!/usr/bin/python3
"""
0-rectangle

"""


class Rectangle:
    """Defines an empty rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the private width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the private height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate perimeter"""
        return (self.__height + self.__width) * 2
