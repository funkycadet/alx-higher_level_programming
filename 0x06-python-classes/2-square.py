#!/usr/bin/python3
"""2-square module

This module defines a square based on 1-square.py by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0) where:
    -size must be an integer, otherwise raise a TypeError exception message:
     'size must be an integer'
    - if size less than 0, raise a ValueError exception with the message:
     'size must be >= 0
- Without importing any module

"""


class Square:
    """class Square

    This is a class that defines a square with a private size

    Methods
    -------
    __init__(self, Square__size):
        An empty module for the class Square

    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size
        """size_is_integer function

        This function checks if:
        - size is < 0
        - size is not an integer

        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
