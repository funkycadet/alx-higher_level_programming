#!/usr/bin/python3
""" Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class which inherits from BaseGeometry """

    def __init__(self, width, height):
        """ __init__ method to initialize instances """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # self.area(width, height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area method to return area """
        return self.__width*self.__height

    def __str__(self):
        """ str method to return printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
