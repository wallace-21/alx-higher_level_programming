#!/usr/bin/python3
"""define a functon called lookup with one arguments"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object

    Args:
    obj: attributes_and_methods
    """
    return (dir(obj))
