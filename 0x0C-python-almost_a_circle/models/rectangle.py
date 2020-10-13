#!/usr/bin/python3
"""rectangle class"""


from models.base import Base


class Rectangle(Base):
    """define the class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter for class"""
        return self.width

    @width.setter
    def width(self, width):
        """setter width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self, x):
        """ getter of X """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter of X """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter of Y """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter of Y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """function to return the area"""
        return self.__width * self.height

    def display(self):
        """Prints in stdout with character #"""
        print("\n" * self.__y, end="")
        print(((" " * self.__x) + ("#" * self.__width) + "\n")*self.__height,
        end="")
