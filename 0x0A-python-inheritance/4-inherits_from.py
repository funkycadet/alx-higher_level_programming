#!/usr/bin/python3
"""
4-inherits_from module
  - contains inherits_from function
"""


def inherits_from(obj, a_class):
    """ inherits_from function """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
