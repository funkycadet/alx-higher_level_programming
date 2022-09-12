#!/usr/bin/python3
"""
7-base_geometry module
  - contains class BaseGeometry
    - BaseGeometry contains area method
    - BaseGeometry contains integer_validation method
"""


class BaseGeometry:
    """ empty class BaseGeometry"""

    def area(self):
        """ area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ integer_validation method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
