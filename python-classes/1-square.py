#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """A class that represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
