#!/usr/bin/python3
"""1-square module
This module defines a square based on 0-square.py by:
- Private instance attribute: size
- Instantiation with size(no type/value verification)
- Without importing any module
"""


class Square:
    """class Square

    This is a class that defines a square with a private size

    """
    __size = 0

    def __init__(self, Square__size):
        self.__size = Square__size
