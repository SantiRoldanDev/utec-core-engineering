#!/usr/bin/env python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an Exception: area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): name of the parameter, used in error messages.
            value: value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
