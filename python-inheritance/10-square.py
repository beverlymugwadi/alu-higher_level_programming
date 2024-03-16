#!/usr/bin/python3
"""A class that inherit from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):


    def __init__(self, size):
        """isinstantiation of a square"""
        super().__init__(size, size)
        size.integer_validator("size", size)
        self._size=size


    def area(self):
        """Return the are of a square"""
        return self._size**2
