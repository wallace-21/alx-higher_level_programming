#!/usr/bin/python3
""" define load_from_json_file """

import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”:

    Args:
        filename: name of the file being used
    """
    with open(filename, 'r', encoding='utf-8') as file:

        return json.loads(file.read())
