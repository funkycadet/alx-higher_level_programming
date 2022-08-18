#!/usr/bin/python3
""" add_integer function """


def add_integer(a, b=98):
    if type(a) == float:
        a = round(a)
    elif type(b) == float:
        b = round(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
