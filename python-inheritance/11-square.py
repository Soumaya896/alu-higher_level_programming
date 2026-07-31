#!/usr/bin/python3
"""
This module contains a Square class inheriting from Rectangle with formatting.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle and formats output as a Square.
    """

    def __init__(self, size):
        """
        Instantiates the square with a validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the print-friendly string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
