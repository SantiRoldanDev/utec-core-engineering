#!/usr/bin/env python3
"""Defines the Square class, which inherits from Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by a private size (width == height)."""

    def __init__(self, size):
        """Initialize a Square after validating size.

        Args:
            size (int): positive integer side length.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
