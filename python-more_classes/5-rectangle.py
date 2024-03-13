#!/usr/bin/python3
"""Defining class"""

class Rectangle:

    """Initialization"""
    def __init__(self,width=0,height=0):
        self._width=width
        self._height=height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        elif value<0:
            raise ValueError("width must be >=o")
        self._width=value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        elif value<0:
            raise ValueError("width must be>=0")
        self.height=value

    def area(self):
        """Returning the area of a rectangle"""
        return self._width*self._height

    def perimeter(self):
        """Returning the perimeter of a rectangle"""
        if self._width==0 and self._height==0:
            return 0
        else:
            return (self._width)+(self._height)

    def __str__(self):
        """Returning a printable presentation of a rectangle
        Represent the rectangle with the '#' character"""
        if self._width==0 or self._height==0:
            return"0"

        rect=[]
        for i in range (self._height):
            rect.append('#'*self._width)
            if i!=self._height-1:
                rect.append("\n")
        return"".join(rect)

    def __repr__(self):
        """Returning the sring presentation of a rectangle"""
        return "Rectangle (" + str(self._width) + "," + str(self._height) + ")"

    def __del__(self):
        return "Bye rectangle..."
