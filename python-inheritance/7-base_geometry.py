#!/usr/bin/python3
"""Defining BaseGeometry Class."""


class BaseGeometry:
    """represent a geometry."""

    def area(self):
        """raise an exception message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if the value is an integer greater that 0"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")