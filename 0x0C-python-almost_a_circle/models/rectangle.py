#!/usr/bin/python3
"""
rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    define the class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validator(name, value):
        """Validator of all setter methods and instantiation"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """function to return the area"""
        return self.__width * self.height

    def display(self):
        '''method to print'''
        dis1 = '\n' * self.__y
        dis2 = (((' ' * self.__x) + '#' * self.__width + '\n') * self.__height)
        print(dis1 + dis2[:-1])

    def __str__(self):
        """string representation"""
        i1 = '(' + str(self.id) + ') ' + str(self.__x) + '/'
        i2 = str(self.__y) + ' - ' + str(self.__width)
        return "[Rectangle] " + i1 + i2 + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in ['id', 'width', 'height', 'x', 'y']:
                    setattr(self, key, value)
        elif args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
