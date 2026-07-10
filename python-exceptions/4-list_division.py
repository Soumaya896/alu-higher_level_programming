#!/usr/bin/python3
"""Module that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide my_list_1 by my_list_2 element-wise up to list_length."""
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(result)
    return new_list
