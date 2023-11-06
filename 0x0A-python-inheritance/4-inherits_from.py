#!/usr/bin/python3
"""A function with two arguments """


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: object.
        a_class: A class

    Returns:
           True if obj is an instance of a class that inherits
           from a_class (directly or indirectly), otherwise False.
    """
    return (issubclass(type(obj), a_class))
