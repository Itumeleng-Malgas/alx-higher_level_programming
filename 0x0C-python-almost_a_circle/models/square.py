#!/usr/bin/python3
""" implements the square, as a sub class of rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class implementation """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize the square class """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """ prints a formatted view of a square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ size attribute getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size attribute setter """
        self.width = value
        self.height = value
