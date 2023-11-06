#!/usr/bin/python3
""" a function with two arguments """


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an
    instance of the specified class

    Args:
        obj: a list
        a_class: a class

    Returns:
           True if obj is exactly an instance of a_class, otherwise False
    """
    return (type(obj) is a_class)
