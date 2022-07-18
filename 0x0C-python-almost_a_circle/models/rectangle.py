#!/usr/bin/python3
"""rectangle module

This module holds class Rectangle which:
- inherits the Base class

- private instance attributes, each with its own public getter and setter:
    - __width -> width
    - __height -> height
    - __x -> x
    - __y -> y

- class construct def __init__(self, width, height, x=0, y=0, id=None) which:
    - calls the super class with id - this super call with use the logic of
      the __init__ of the Base class
    - assigns each argument width, height, x and y to the right attribute

"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle

    This class is used to create objects with attributes to that of a rectangle

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method

        This method is used to initialize id inherited from class Base

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width method

        Method to return the width property

        """
        return self.__width

    @width.setter
    def width(self, value):
        """width.setter method

        Method to set the width

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height method

        Method to return the height property

        """
        return self.__height

    @height.setter
    def height(self, value):
        """height.setter method

        Method to set the height

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x method

        Method used to retrieve x property

        """
        return self.__x

    @x.setter
    def x(self, value):
        """x.setter method

        Method to set x

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y method

        Method used to retrieve y property

        """
        return self.__y

    @y.setter
    def y(self, value):
        """y.setter method

        Method to set y

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area method

        Method that returns the area value of a Rectangle instance

        """
        return self.width * self.height

    def display(self):
        """display method

        Method that prints in stdout a Rectangle instance with the character #

        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """__str__ method

        Method that prints an instance of Rectangle object

        """
        _str_rectangle = "[Rectangle] "
        _str_id = "({}) ".format(self.id)
        _str_xy = "{}/{} ".format(self.x, self.y)
        _str_wh = "- {}/{}".format(self.width, self.height)

        return _str_rectangle + _str_id + _str_xy + _str_wh

    def update(self, *args, **kwargs):
        """update method

        Method that uses *args, a no-keyword argument to assign arguments to
        attributes

        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary method

        Method to return a dictionary with properties

        """
        list_att = ['x', 'y', 'id', 'height', 'width']
        new_dict = {}

        for key in list_att:
            new_dict[key] = getattr(self, key)
        return new_dict
