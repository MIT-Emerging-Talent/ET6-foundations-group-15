#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for largest_perfect_square_less_than function.

Contains tests for checking the functionality of finding

the largest perfect square less than a given number.

Test categories:

    - Functionality tests: checking if the function correctly identifies
    the largest perfect square less than a number.

    - Edge tests:
        - Small positive numbers (the input is less than or equal to 1)
        - Perfect squares and slightly below or above it
        - Very large numbers
        - Zero

    - Defensive tests: ensuring the function handles invalid inputs such as:
        - Negative numbers
        - Non-numeric inputs


Created on 2025-01-06
@author: Huda Alamassi
"""

import unittest

from solutions.largest_perfect_square_less_than_number import (
    largest_perfect_square_less_than_number,
)


class TestLargestPerfectSquareLessThanNumber(unittest.TestCase):
    """Test the largest_perfect_square_less_than_number function."""

    # Test functionality
    def test_integer_input(self):
        """It should return the largest perfect square less than the given integer."""
        actual = largest_perfect_square_less_than_number(50)
        self.assertEqual(actual, 49)

    def test_float_input(self):
        """It should return the largest perfect square less than the given float."""
        actual = largest_perfect_square_less_than_number(2.6)
        self.assertEqual(actual, 1)

    # Test edge cases
    def test_small_positive_number(self):
        """It should return 0 when the input is less than or equal to 1."""
        actual = largest_perfect_square_less_than_number(0.5)
        self.assertEqual(actual, 0)

    def test_perfect_square(self):
        """It should return the largest perfect square less than the given perfect square."""
        actual = largest_perfect_square_less_than_number(16)
        self.assertEqual(actual, 9)

    def test_slightly_above_perfect_square(self):
        """It should return the largest square less than input slightly above a perfect square."""
        actual = largest_perfect_square_less_than_number(16.5)
        self.assertEqual(actual, 9)

    def test_slightly_below_perfect_square(self):
        """It should return the largest square less than input slightly below a perfect square."""
        actual = largest_perfect_square_less_than_number(15.9)
        self.assertEqual(actual, 9)

    def test_very_large_number(self):
        """It should return the largest perfect square less than a very large input."""
        actual = largest_perfect_square_less_than_number(10**6)
        self.assertEqual(actual, 998001)

    def test_zero(self):
        """It should return 0 when the input is 0."""
        actual = largest_perfect_square_less_than_number(0)
        self.assertEqual(actual, 0)

    # Test defensive assertions
    def test_defensive_assertion_for_negative_input(self):
        """It should raise an AssertionError when the input is negative."""
        with self.assertRaises(AssertionError):
            largest_perfect_square_less_than_number(-10)

    def test_defensive_assertion_for_non_numeric_input(self):
        """It should raise an AssertionError when the input is not a number."""
        with self.assertRaises(AssertionError):
            largest_perfect_square_less_than_number("abc")
