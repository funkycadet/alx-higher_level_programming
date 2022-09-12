#!/usr/bin/python3
""" 100-my_int module"""


class MyInt(int):
    """ class MyInt is a rebel which inherits from int"""

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)
