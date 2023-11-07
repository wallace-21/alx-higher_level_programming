#!/usr/bin/python3
""" define read_file """


def read_file(filename=""):
    """ function that reads a text file

    Args:
        filename: name of the file being used
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
