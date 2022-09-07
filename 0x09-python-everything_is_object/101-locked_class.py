#!/usr/bin/python3
"""

This module contains a class that prevents
dynamic creation of attributes

"""


class LockedClass():
    __names__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
