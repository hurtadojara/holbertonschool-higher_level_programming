#!/usr/bin/python3
char = 97
while (char < 123):
    if char != 113 and char != 101:
        print("{0}".format(chr(char)), end="")
        char = char + 1
    else:
        char = char + 1
