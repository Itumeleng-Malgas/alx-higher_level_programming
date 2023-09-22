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

    def update(self, *args, **kwargs):
        """ updates square class attributes """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
