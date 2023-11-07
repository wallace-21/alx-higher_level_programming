#!/usr/bin/python3
""" define to_json_string """

import json


def to_json_string(my_obj):
    """
    function that eturn the JSON representation of an object as a string.

    Args:
        my_obj: object to be converted to JSON.
    """
    return json.dumps(my_obj)
