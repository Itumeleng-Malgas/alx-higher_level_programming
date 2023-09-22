#!/usr/bin/python3
""" implements a Rectangle, sub class of Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class representation """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle class initialization """
        super().__init__(id)

        self.__width = None
        self.width = width

        self.__height = None
        self.height = height

        self.__x = None
        self.x = x

        self.__y = None
        self.y = y

    # getters and setter for width & height attributes
    @property
    def width(self):
        """ width attribute getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width attribute setter """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ height attribute getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height attribute setter """
        self.integer_validator("height", value)
        self.__height = value

    # getters and setter for x & y attributes
    @property
    def x(self):
        """ x attribute getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x attribute setter """
        self.integer_validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        """ y attribute getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y attribute setter """
        self.integer_validator("y", value, True)
        self.__y = value

    def area(self):
        """ computes the area of a rectangle """
        return self.width * self.height

    def display(self):
        """ displays attributes of a rectangle """
        for _ in range(self.y):
            print()
        rect = [' ' * self.x + '#' * self.width for _ in range(self.height)]
        print('\n'.join(rect))

    def __str__(self):
        """ prints a formatted view of a rectangle """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """ updates rectangle attributes """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ returns dict representation of class Rectangle """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
