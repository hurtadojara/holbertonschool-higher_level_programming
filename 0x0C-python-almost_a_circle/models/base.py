#!/usr/bin/python3
"""base for objects"""


class base:
    """base for all point in the proyect"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
