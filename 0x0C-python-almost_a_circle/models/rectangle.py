#!/usr/bin/python3
""" implements a Rectangle, sub class of Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class representation """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle class initialization """
        super().__init__(id)

        self._width = None
        self.width = width

        self._height = None
        self.height = height

        self._x = None
        self.x = x

        self._y = None
        self.y = y

    # getters and setter for width & height attributes
    @property
    def width(self):
        """ width attribute getter """
        return self._width

    @width.setter
    def width(self, value):
        """ width attribute setter """
        self.integer_validator("width", value)
        self._width = value

    @property
    def height(self):
        """ height attribute getter """
        return self._height

    @height.setter
    def height(self, value):
        """ height attribute setter """
        self.integer_validator("height", value)
        self._height = value

    # getters and setter for x & y attributes
    @property
    def x(self):
        """ x attribute getter """
        return self._x

    @x.setter
    def x(self, value):
        """ x attribute setter """
        self.integer_validator("x", value, True)
        self._x = value

    @property
    def y(self):
        """ y attribute getter """
        return self._y

    @y.setter
    def y(self, value):
        """ y attribute setter """
        self.integer_validator("y", value, True)
        return self._y
