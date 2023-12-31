#!/usr/bin/python3
""" define class base """

from models.base import Base
""" import Base """


class Rectangle(Base):
    """ a class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize an instance of Rectangle.
        Args:
            width: the width value
            height: the height vlaue
            x: x-coordinate value
            y: y-coordinate value
        """
        if not isinstance(width, int):

            raise TypeError("width must be an integer")

        if not isinstance(height, int):

            raise TypeError("height must be an integer")

        if not isinstance(x, int):

            raise TypeError("x must be an integer")

        if not isinstance(y, int):

            raise TypeError("y must be an integer")

        if y < 0:

            raise ValueError("y must be >= 0")

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter for the width attribute """

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:

            raise TypeError("width must be an integer")

        if value <= 0:

            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ setter for the height attribute """

        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:

            raise TypeError("height must be an integer")

        if value <= 0:

            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter for the x-coordinate attribute """
        return self.__x

    @x.setter
    def x(self, value):

        if type(value) is not int:

            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for the x-coordinate attribute """
        return self.__y

    @y.setter
    def y(self, value):

        if type(value) is not int:

            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of Rectangle"""

        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """

        for i in range(self.__y):

            print()

        for i in range(self.__height):

            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ overriding the __str__ method """

        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """  assigns an argument to each attribute """

        if len(args) >= 1:

            self.id = args[0]

        if len(args) >= 2:

            self.__width = args[1]

        if len(args) >= 3:

            self.__height = args[2]

        if len(args) >= 4:

            self.__x = args[3]

        if len(args) >= 5:

            self.__x = args[4]

        else:
            for key, value in kwargs.items():

                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
