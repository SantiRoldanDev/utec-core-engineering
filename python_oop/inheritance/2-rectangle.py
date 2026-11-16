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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
