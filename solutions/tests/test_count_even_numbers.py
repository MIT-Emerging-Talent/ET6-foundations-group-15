#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains unit tests for the `count_evens` function.

Author: Norbert Ndayisenga
Date: 07 01 2024
"""

import unittest
from ..count_even_numbers import count_evens 

class TestCountEvens(unittest.TestCase):
    """
    Unit tests for the `count_evens` function.
    """

    def test_empty_list(self):
        """Test that an empty list returns 0."""
        self.assertEqual(count_evens([]), 0)

    def test_no_even_numbers(self):
        """Test that a list with no even numbers returns 0."""
        self.assertEqual(count_evens([1, 3, 5]), 0)

    def test_all_even_numbers(self):
        """Test that a list with all even numbers returns the correct count."""
        self.assertEqual(count_evens([2, 4, 6]), 3)

    def test_mixed_numbers(self):
        """Test that a list with mixed even and odd numbers returns the correct count."""
        self.assertEqual(count_evens([1, 2, 3, 4, 5, 6]), 3)

    def test_negative_numbers(self):
        """Test that negative even numbers are correctly counted."""
        self.assertEqual(count_evens([-2, -4, 3, 5]), 2)

    def test_mixed_types(self):
        """Test that a list with mixed types counts only even integers."""
        self.assertEqual(count_evens([1, 2, "string", 3.5, None, 4]), 2)

    def test_invalid_input(self):
        """Test that invalid inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            count_evens("string")

        with self.assertRaises(TypeError):
            count_evens(123)

