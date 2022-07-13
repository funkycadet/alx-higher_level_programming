#!/usr/bin/python3
"""6-square module

This module defines a square based on 3-square.py by:
- Private instance attribute: size where:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
      - size must be an integer, otherwise raise a TypeError exception message:
         'size must be an integer'
      - if size less than 0, raise a ValueError exception with the message:
         'size must be >= 0'

- Private instance attribute: position:
    - property def position(self): to retrieve it
    - property setter def position(self, value): to set it:
      - position must be a tuple of 2 positive integers, otherwise
        raise a TypeError exception with the message:
         'position must be a tuple of 2 positive integers'

- Instantiation with optional size:
    def __init__(self, size=0, position=(0, 0)):

- Public instance method: def area(self): that returns the current square area

- Public instance method: def my_print(self): that prints in stdout the square
  with character '#':
    - if size is equal to 0, print an empty line
    - position should be use by using space
    - don't fill lines by spaces when position[1] > 0

- without importing any module

"""


class Square:
    """class Square

    This is a class that defines a square with a private size

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        """__init__ method

        This method initializes the size and position argument

        """

    @property
    def size(self):
        """size method

        This is used to retrieve the property of size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size.setter method

        This method is used to set the size value of the square object

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """property method

        This is used to retrieve the property of position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position.setter method

        This method is used to set the position value of the square object

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area method

        This method returns the current square area

        """
        return self.__size ** 2

    def my_print(self):
        """my_print method

        This method prints a # square according to size value

        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print('#', end='')
                print()
