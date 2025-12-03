#!/usr/bin/python3
"""
Defines the Rectangle class that extends BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Width and height validated as positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes Rectangle dimensions after validation.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
