#!/usr/bin/python3
"""1-square module

This module defines a square based on 0-square.py by:
- Private instance attribute: size

- Instantiation with size(no type/value verification)

- without importing any module

"""


class Square:
    """class Square

    This is a class that defines a square with a private size

    """
    # __size = 0

    def __init__(self, __size):
        """__init__ method

        This method initializes the size argument

        """
        self.__size = __size
