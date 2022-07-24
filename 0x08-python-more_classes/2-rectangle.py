#!/usr/bin/python3
"""1-rectangle module

This module defines a rectangle based on 0-rectangle by:
- Private instance attribute: width
    - property def width(self): to retrieve it
    - property setter def width(self, value): to set it:
     - width must be an integer, otherwise raise a TypeError exception message:
         'width must be an integer'
      - if width is less than 0, raise a ValueError exception message:
         'width must be >= 0'

- Private instance attribute: height:
    - property def height(self): to retrieve it
    - property setter def height(self, value): to set it:
    - height must be an integer, otherwise raise a TypeError exception message:
         'height must be an integer'
      - if height is less than 0, raise a ValueError exception message:
         ' height must be >= 0'

- Instantiation with optional width and height:
    def __init__(self, width=0, height=0):

- Public instance method: def area(self): that returns the rectangle area

- Public instance method: def perimeter(self):
  that returns the rectangle perimeter:
    - if width or height is equal to 0, perimeter is equal to 0

- Without importing any module

"""


class Rectangle:
    """class Rectangle

    This is an empty class that defines a rectangle

    """

    def __init__(self, width=0, height=0):
        """__init__ method

        Method to initialize width and height argument(s)

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """width method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width.setter method
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height.setter method
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area method
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter method
        """
        return 2*(self.width + self.height)
