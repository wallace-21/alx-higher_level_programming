#!/usr/bin/python3
""" A function with two arguments """


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it's an
    instance of a class that inherited from, the specified class.

    Args:
        obj: object.
        a_class: A class

    Returns:
           True if obj is an instance of, or inherits from,
           a_class, otherwise False.
    """
    return isinstance(obj, a_class)
