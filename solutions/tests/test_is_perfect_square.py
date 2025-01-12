#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for is_perfect_square function.

Contains tests for checking if a number is a perfect square, handling edge cases, and ensuring
proper input validation.

Test categories:
    - Functionality tests: checking if the function correctly identifies perfect squares
    - Edge cases: testing with `0`, negative numbers, and large numbers
    - Defensive tests: incorrect input types such as non-numeric values

Created on 2025-01-10
Author: Huda Alamassi
"""

import unittest

from solutions.is_perfect_square import is_perfect_square


class TestIsPerfectSquare(unittest.TestCase):
    """Test the is_perfect_square function."""

    # Functionality Tests
    def test_perfect_square(self):
        """It should return True for perfect squares."""
        actual = is_perfect_square(16)
        self.assertEqual(actual, True)

    def test_non_perfect_square(self):
        """It should return False for non-perfect squares."""
        actual = is_perfect_square(17)
        self.assertEqual(actual, False)

    def test_float_perfect_square(self):
        """It should return True for float values that are perfect squares."""
        actual = is_perfect_square(25.0)
        self.assertEqual(actual, True)

    def test_float_non_perfect_square(self):
        """It should return False for float values that are not perfect squares."""
        actual = is_perfect_square(18.5)
        self.assertEqual(actual, False)

    # Edge Tests

    def test_zero(self):
        """It should return True for 0, as it is a perfect square."""
        actual = is_perfect_square(0)
        self.assertEqual(actual, True)

    def test_negative_number(self):
        """It should return False for negative numbers, as they cannot be perfect squares."""
        actual = is_perfect_square(-9)
        self.assertEqual(actual, False)

    def test_large_perfect_square(self):
        """It should return True for large perfect squares."""
        actual = is_perfect_square(1000000)
        self.assertEqual(actual, True)

    def test_large_non_perfect_square(self):
        """It should return False for large non-perfect squares."""
        actual = is_perfect_square(1000001)
        self.assertEqual(actual, False)

    # Defensive Tests
    def test_defensive_assertion_for_non_number_input(self):
        """It should raise an assertion error if the input is not a number."""
        with self.assertRaises(AssertionError):
            is_perfect_square("string")

    def test_defensive_assertion_for_non_numeric_input(self):
        """It should raise an assertion error if the input is not a number."""
        with self.assertRaises(AssertionError):
            is_perfect_square([1, 2, 3])
