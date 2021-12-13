#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""

class Rectangle:
    """A Rectangle class with attributes  width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
    
    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
