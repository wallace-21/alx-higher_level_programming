#!/usr/bin/python3
""" define save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text
    file, using a JSON representatio

    Args:
        my_obj: object to be saved as JSON.
        filename: name of the file being used
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
