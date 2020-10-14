#!/usr/bin/python3
"""
base for objects
"""


class Base:
    """
    base for all point in the proyect
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        '''
        staticmethod from_json_string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        staticmethod to_json_string
        '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
