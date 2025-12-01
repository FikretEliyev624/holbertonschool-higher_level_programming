#!/usr/bin/python3
"""
0-rectangle

"""


class Rectangle:
    """Defines an empty rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Return printable rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return official string representation to recreate instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
