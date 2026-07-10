#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print value as an integer; return True if successful."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
