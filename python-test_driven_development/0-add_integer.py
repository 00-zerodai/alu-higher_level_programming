#!/usr/bin/python3
"""Provide a function for adding integer values."""


def add_integer(a, b=98):
    """Add two numbers after converting integer-compatible inputs."""
    if type(a) is bool or type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) is bool or type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
