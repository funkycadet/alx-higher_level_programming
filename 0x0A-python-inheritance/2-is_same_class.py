#!/usr/bin/python3
"""
2-is_same_class module
  - contains is_same_class function
"""


def is_same_class(obj, a_class):
    """ is_same_class function """
    if a_class == type(obj):
        return True
    else:
        return False
