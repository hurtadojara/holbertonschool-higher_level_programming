#!/usr/bin/python3
''' read linessssss '''


def read_lines(filename="", nb_lines=0):
    """
    readlines
    """
    i = 0
    j = 0
    lines = ""
    with open(filename, mode="r", encoding="utf-8") as leer:
        if nb_lines == 0:
            print(leer.read())
        elif nb_lines <= 0 or nb_lines > 0:
            for i in range(nb_lines):
                lines = leer.readline()
                print("{}".format(lines), end="")
