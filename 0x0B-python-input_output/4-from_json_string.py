#!/usr/bin/python3
""" define "from_json_string """

import json


def from_json_string(my_str):
    """ function that returns an object
    (Python data structure) represented by a JSON string

    Args:
        my_str:  string to represented
    """
    return json.loads(my_str)
