#!/usr/bin/python3
"reads a file"


def read_file(filename=""):
    """
    reads file
    """
    with open(filename, mode="r", encoding="utf-8") as leer:
        print(leer.read())
