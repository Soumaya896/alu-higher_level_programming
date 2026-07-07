#!/usr/bin/python3
"""Module that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    length = len(my_list)
    for i in range(length - 1, -1, -1):
        print("{:d}".format(my_list[i]))
