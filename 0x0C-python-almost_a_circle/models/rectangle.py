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

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value <= 0
        :
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ setter for the height attribute """

        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):

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

        if not isinstance(value, int):

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

        if not isinstance(value, int):

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
