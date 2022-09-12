#!/usr/bin/python3
"""
3-is_kind_of_class module
  - contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class function """
    if isinstance(obj, a_class):
        return True
    else:
        return False
