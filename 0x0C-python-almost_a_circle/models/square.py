#!/usr/bin/python3
"""square inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor init for the Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size

    def __str__(self):
        """string representation"""
        i1 = '(' + str(self.id) + ') ' + str(self.x) + '/'
        i2 = str(self.y) + ' - ' + str(self.width)
        return "[Square] " + i1 + i2

    def update(self, *args, **kwargs):
        """method to update attributes by args"""
        attr = ['id', 'size', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
