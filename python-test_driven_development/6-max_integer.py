#!/usr/bin/python3
"""Provide a function for finding the maximum integer in a list."""


def max_integer(list=[]):
    """Return the largest list value, or None when the list is empty."""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
