#!/usr/bin/python3
"""base module

This module holds class Base with:
- private class attribute __nb_objects = 0

- class constructor: def __init__(self, id=None): where:
    - if id is not None, it assigns the public instance
      attribute id with this argument value - id would be
      assumed to be an integer and its nt a must to test it
    - otherwise, __nb_objects is incremented and a new value
      is assigned to the public instance attribute id

"""


class Base:
    """class Base

    This class is used to manage id attribute in all future
    classes and to avoid duplication of the same code (by
    extensions, same bugs)

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method

        Method used to initialize id and __nb_objects args

        """
        # self.__nb_objects = __nb_objects
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
