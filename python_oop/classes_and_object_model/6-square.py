#!/usr/bin/env python3
"""This module defines a class Square with a size and a position."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a validated size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The (x, y) offset of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating it.

        Args:
            value (tuple): A tuple of 2 positive integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character, or an empty line if 0."""
        print(self)

    def __str__(self):
        """Return the square drawn with # and offset by its position."""
        if self.__size == 0:
            return ""
        x, y = self.__position
        lines = [""] * y
        lines += [" " * x + "#" * self.__size for _ in range(self.__size)]
        return "\n".join(lines)
