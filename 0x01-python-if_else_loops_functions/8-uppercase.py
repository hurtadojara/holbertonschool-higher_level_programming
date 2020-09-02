#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if i < 'z' and i >= 'a':
            result += chr(ord(i) - 32)
        else:
            result += i
    print(result)
