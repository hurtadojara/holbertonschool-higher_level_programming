#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """
    writes to fl
    """
    i = 0
    with open(filename, mode="w", encoding="utf-8") as archivo:
        archivo.write(text)
    with open(filename, mode="r", encoding="utf-8") as archivo:
        for line in archivo:
            for letter in line:
                i = i + 1
        return i
