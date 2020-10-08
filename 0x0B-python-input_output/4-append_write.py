#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    '''
    function to append_write to a file
    '''
    with open(filename, mode="a", encoding="utf-8") as archivo:
        archivo.write(text)
        i = 0
        for chars in text:
            i = i + 1
        return i
