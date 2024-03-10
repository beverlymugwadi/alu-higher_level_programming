#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""
class Rectangle:
    """initialization"""
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            if not isinstance(int,value):
                raise TypeError("width must be an integer")
            elif value<0:
                raise ValueError("width must be >= 0")
            else:
                self._width=value


        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, value):
            if not isinstance(int,value):
                raise TypeError("height must be an integer")
            elif value<0:
                raise ValueError("height must be >= 0")
            else:
                self._height=value

        def area(self):
            return self.width*self.height

        def perimeter(self):
            return self.widht+self.width+self.height+self.height

