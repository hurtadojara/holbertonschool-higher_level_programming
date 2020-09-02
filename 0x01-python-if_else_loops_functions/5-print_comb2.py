#!/usr/bin/python3
i = 0
for i in range(100):
    if i == 99:
        print("{0}".format(i))
    print("{:02d}, ".format(i), end="")
