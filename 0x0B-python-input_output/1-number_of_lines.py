#!/usr/bin/python3
"""read number of lines and prints it"""


def number_of_lines(filename=""):
    """
    reads number of lines and print it
    """
    i = 0
    with open(filename, mode="r", encoding="utf-8") as lineas:
        for a, b in enumerate(lineas):
            i += 1
            pass
    return i
