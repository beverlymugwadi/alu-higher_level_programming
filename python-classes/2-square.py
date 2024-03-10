#!/usr/bin/python3

"""Creating Class Square"""
class Square:
    
    
    """
    instantiate the class 
    
    """
    
    def __init__(self, size=0):
         
        """init size"""
         
        if not isinstance(size,int):
            raise TypeError ("Size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >=0")
        
        self.size=size
