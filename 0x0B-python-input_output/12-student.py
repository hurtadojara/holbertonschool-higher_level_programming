#!/usr/bin/python3
'''module class Student'''


class Student:
    '''
    Student class
    '''
    def __init__(self, first_name, last_name, age):
        '''
        init function of the class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        function to_json
        '''
        if attrs is None:
            return self.__dict__
        if all(isinstance(at, str) for at in attrs):
            if isinstance(attrs, list):
                return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
