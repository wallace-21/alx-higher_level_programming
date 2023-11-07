#!/usr/bin/python3
""" define a Rectangle """


class BaseGeometry:
    """Represent a Rectangle """

    def area(self):
        """ raises some exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """" integer_validator

        Args:
            name: name
            value: value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ inherince"""
    def __init__(self, width, height):
        """
        Initialize a Rectangle

        Args:
            width Width of the rectangle (must be a positive integer).
            height: Height of the rectangle (must be a positive integer).
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
