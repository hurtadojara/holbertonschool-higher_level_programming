#!/usr/bin/python3
'''class "rectangle" '''


class Rectangle:
    """
    represent a rectangle
    _
    Attributes
    ----------
    width : int
        width of the rectangle
    height : int
        height of the rectangle
    number_of_instances = int
        +1 en instance
        -1 on delete
    print_symbol = str
        symbol to print the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
    '''getter width'''
    @property
    def width(self):
        return self.__width
    ''' setter width '''
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    '''getter height'''
    @property
    def height(self):
        return self.__height
    ''' setter size '''
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    '''method to calculate the area of the rectangle'''
    def area(self):
        return self.__width * self.__height
    '''method to calculate the perimeter of the rectangle'''
    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    '''method print the rectangle'''
    def __str__(self):
        if self.__height is 0 or self.__width is 0:
            return ""
        pic = (str(self.print_symbol) * self.__width + "\n") * self.__height
        return pic[:-1:]
    '''method to return the representation of Rectangle'''
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    '''method to delete a Rectangle instance'''
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
