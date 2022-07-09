#!/usr/bin/python3
"""3-square module

This module defines a square based on 2-square.py by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0) where:
    -size must be an integer, otherwise raise a TypeError exception message:
     'size must be an integer'
    - if size less than 0, raise a ValueError exception with the message:
     'size must be >= 0'
- Public instance method: def area(self): that returns the current square area
- Without importing any module

"""


class Square:
    """class Square

    This is a class that defines a square with a private size

    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size
        """__init__ method

        This method initializes the size argument and checks if:
        - size is < 0
        - size is not an integer

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
    
    def area(self):
        """area method

        This method returns the current square area

        """
        area = self.__size
        return area*area
