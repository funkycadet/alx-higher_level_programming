#!/usr/bin/python3
"""square module

This module holds the Square class which:
- inherits the Rectangle class

- constructor def __init__(self, size, x=0, y=0, id=None):
    - call super class with id, x, y, width and height which will:
     - use the logic of the __init__ of Rectangle class
     - its width and height must be assigned to size
    - no new attributes as only attributes of Rectangle class would be used
     (remember that a Square is a rectangle with same height and width)
    - all width, height, x and y validation must inherit from Rectangle
     and would display same behavior in cases of wrong data

- its overloading __str__ method would return [Square] (<id>) <x>/<y> - <size>
 (in this case, it would be width or height)

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square

    This class is used to create objects with attributes of a real-world Square

    """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method

        Method that initializes properties inherited from Rectangle

        """
        # self.width = self.height = size
        # self.height = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__method

        Method that prints an instance of Square objects

        """
        _str_square = "[Square] "
        _str_id = "({}) ".format(self.id)
        _str_xy = "{}/{} ".format(self.x, self.y)
        _str_w = "- {}".format(self.width)

        return _str_square + _str_id + _str_xy + _str_w
        # return super().__str__()

    @property
    def size(self):
        """size method

        Method to retrieve size property

        """
        return self.width

    @size.setter
    def size(self, value):
        """size.setter method

        Method to set size

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        """
        return super().update(*args, **kwargs)

    def to_dictionary(self):
        """to_dictionary method

        Method to return Square instance properties in a dictionary

        """
        list_att = ['id', 'x', 'size', 'y']
        new_dict = {}
        for key in list_att:
            new_dict[key] = getattr(self, key)
        return new_dict
