#!/usr/bin/python3
"""Unit tests for the max_integer function."""
import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test maximum selection for lists of integers."""

    def test_empty_list(self):
        """Return None for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_default_list(self):
        """Return None when the default empty list is used."""
        self.assertIsNone(max_integer())

    def test_single_value(self):
        """Return the sole value in a one-element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_ascending_values(self):
        """Return the final value from an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_descending_values(self):
        """Return the first value from a descending list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_middle_maximum(self):
        """Find a maximum located between the ends of the list."""
        self.assertEqual(max_integer([1, 5, 3]), 5)

    def test_negative_values(self):
        """Find the greatest value when all values are negative."""
        self.assertEqual(max_integer([-4, -1, -8]), -1)

    def test_repeated_maximum(self):
        """Return the maximum when it appears more than once."""
        self.assertEqual(max_integer([2, 5, 5, 1]), 5)

    def test_list_is_not_modified(self):
        """Leave the input list unchanged."""
        values = [3, 1, 4, 2]
        max_integer(values)
        self.assertEqual(values, [3, 1, 4, 2])


if __name__ == "__main__":
    unittest.main()
