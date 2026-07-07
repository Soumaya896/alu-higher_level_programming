#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, each row on its own line."""
    for row in matrix:
        line = ""
        for i in range(len(row)):
            line += "{:d}".format(row[i])
            if i != len(row) - 1:
                line += " "
        print(line)
