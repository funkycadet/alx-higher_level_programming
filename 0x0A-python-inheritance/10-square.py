#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class which inherits from Rectangle """

    def __init__(self, size):
        """ __init__ method to initialize instances """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ area method to return area of square """
        return super().area()
