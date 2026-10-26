#!/usr/bin/env python3
"""Module that provides a function to read a text file and print it."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
