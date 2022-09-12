#!/usr/bin/python3
"""
0-lookup module that contains the lookup function
which returns a list of available attributes and
methods of an object
"""


def lookup(obj):
    """ lookup function """
    return dir(obj)
