#!/usr/bin/python3
""" define write_file """


def write_file(filename="", text=""):
    """  function that writes a string to a text file

    Args:
        filename: name of the file being used
        text: text to be added
    """
    with open("filename", "w", encoding='utf-8') as file:

        return (file.write(text))
