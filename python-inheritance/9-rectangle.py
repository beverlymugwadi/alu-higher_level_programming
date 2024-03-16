#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if the value is an integer greater that 0"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """Implememnting area"""
    def area(self):
        return self._width * self.__height

    """The presentation should be string"""
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
