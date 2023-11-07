#!/usr/bin/python3
""" BaseGeometry module"""


class BaseGeometry:
    """ define  BaseGeometry """

    def area(self):
        """
        The area

        Raises:
              Exception: Always raises an exception with them
              message "area() is not implemented."
        """
        raise Exception("area() is not implemented")
