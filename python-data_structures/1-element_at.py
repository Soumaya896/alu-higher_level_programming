#!/usr/bin/python3
"""Module that retrieves an element from a list like in C."""


def element_at(my_list, idx):
    """Retrieve the element at idx, or None if idx is invalid."""
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
