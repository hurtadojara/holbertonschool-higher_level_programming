#!/usr/bin/python3
"""This module writes a class Square that defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize the data
        Args:
            size: size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
