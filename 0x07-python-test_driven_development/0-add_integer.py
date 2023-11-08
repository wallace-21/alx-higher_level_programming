#!/usr/bin/python3
""" define add_integer """


def add_integer(a, b=98):
    """ function that adds 2 integers

    Args:
        a: integer to be added
        b: integer to be added
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):

        if isinstance(a, float):
            a = int(a)

        if isinstance(b, float):
            b = int(b)

        return (a + b)

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
