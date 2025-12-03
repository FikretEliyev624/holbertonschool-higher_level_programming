#!/usr/bin/python3
"""
Rectangle module - extended
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
