#!/usr/bin/python3
"""Module that replaces an element in a copy of a list."""


def new_in_list(my_list, idx, element):
    """Return a copy of my_list with the element at idx replaced."""
    new_list = my_list[:]
    if idx < 0 or idx > len(new_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
