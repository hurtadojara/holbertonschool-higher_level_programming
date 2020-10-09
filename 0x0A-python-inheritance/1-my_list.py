#!/usr/bin/python3
"""
class list that inherits
"""


class MyList(list):
    """
    Sclass of list
    """
    def __init__(self):
        """
        Initializace instance of method
        """
        super().__init__

    def print_sorted(self):
        """
        sort
        """
        print(sorted(self))
