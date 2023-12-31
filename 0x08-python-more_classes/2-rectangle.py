#!/usr/bin/python3

""" Define a class rectangle"""


class Rectangle:

    """Represent a rectangle."""

    def __init__(self, width=0, height=0):

        """Constructor for the Rectangle class.

        Args:

             width (int): The width of the rectangle

             height (int): The height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):

        """Property for the width of the rectangle."""

        return (self.__width)

    @width.setter
    def width(self, value):

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        if value < 0:

            raise ValueError("size must be >= 0")

        self.__width = value

    @property
    def height(self):

        """Property for the current height of the rectangle."""

        return (self.__height)

    @height.setter
    def height(self, value):

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """ area of the rectangle"""

        return(self.height * self.width)

    def perimeter(self):

        """perimeter of the rectangle"""

        if (self.height == 0 or self.width == 0):

            return (0)
