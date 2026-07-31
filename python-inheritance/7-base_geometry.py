#!/usr/bin/python3
"""
This module contains the BaseGeometry class with area and validation methods.
"""


class BaseGeometry:
    """
    A BaseGeometry class containing an area method and an integer validator.
    """

    def area(self):
        """
        Raises an Exception indicating the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
