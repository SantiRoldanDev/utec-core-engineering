#!/usr/bin/env python3
"""Defines the Rectangle class, which inherits from BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by a private width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle after validating width and height.

        Args:
            width (int): positive integer width.
            height (int): positive integer height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
