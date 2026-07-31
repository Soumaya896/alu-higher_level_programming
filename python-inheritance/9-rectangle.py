#!/usr/bin/python3
"""
This module contains a full Rectangle class inheriting from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry and implements area.
    """

    def __init__(self, width, height):
        """
        Instantiates the rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the print-friendly string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
