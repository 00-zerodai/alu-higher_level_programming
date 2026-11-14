#!/usr/bin/python3
"""Provide a function for printing a square of hash characters."""


def print_square(size):
    """Print a square whose side length is the given size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
