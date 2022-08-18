#!/usr/bin/python3
""" 0-add_integer module"""


def add_integer(a, b=98):
    """ add integer function"""
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
