#!/usr/bin/python3
""" class square that inheriting rectangle class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class inherits from the Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """

        Args:
            size: size
            x: x-coordinate value
            y: y-coordinate value
            id: id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ set the size of the square """

        return self.width

    @size.setter
    def size(self, value):
        """ get the size of the square

        Args:
            value: new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ const """

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
