#!/usr/bin/python3
""" define append_write """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file

    Args:
        filename: name of the file being used
        text: text to append
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
