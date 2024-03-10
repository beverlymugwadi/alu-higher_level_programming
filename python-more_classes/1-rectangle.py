#!/usr/bin/python3
"""Class that defines a rectangle"""
class Rectangle:
"""Initialization"""
def __init__(self,width=0,height=0):
    self.width=width
    self.height=height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
    if not isinstance (int,width):
        raise TypeError("Width must be an integer")
    elif value<0:
        raise ValueError("Width must be >=0")
    else:
        self._width=value

    @property
    def height(self):
    return self._height

    @height.setter
    def width(self,value):
    if no isinstance (int,height):
        raise TypeError("Height is not an integer")
    elif value<0
       raise ValueError("Height must be >=0")
   else:
       self._height=value
