#!/usr/bin/python3
""" define class base """


class Base:
    """ a class that manages id attribute and to
    avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor with 2 arguments

        Args:
            id: identifies instances of Base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
