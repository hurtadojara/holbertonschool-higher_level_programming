#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > -1 and number < 10:
    print("last digit of {0} is {1}".format(number, number))
if number > 10:
    digit = number % 10
    print("last digit of {0} is {1}".format(number, digit), end=" ")
if number < 0:
    number = abs(number)
    digit = number % 10
    print("last digit of {0} is {1}".format(number, digit), end=" ")
if digit >= 0 and digit < 10:
    if digit > 5:
        print("and is greater than 5")
    elif digit == 0:
        print("and is 0")
    elif digit < 6 and number != 0:
        print("and is less than 6 and not 0")
