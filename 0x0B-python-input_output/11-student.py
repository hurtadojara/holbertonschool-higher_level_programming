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
        return self.__dict__
