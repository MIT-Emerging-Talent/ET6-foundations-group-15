#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for count_even_numbers.py
Created on January 4, 2025

Tests the functionality of the count_even_numbers function.

@author: Norbert Ndayisenga
"""

import unittest
from ..count_even_numbers import count_even_numbers


class TestCountEvenNumbers(unittest.TestCase):
    """
    Unit tests for the count_even_numbers function.
    """

    def test_all_even_numbers(self):
        """Tests a list containing only even numbers."""
        self.assertEqual(count_even_numbers([2, 4, 6, 8]), 4)

    def test_no_even_numbers(self):
        """Tests a list containing no even numbers."""
        self.assertEqual(count_even_numbers([1, 3, 5, 7]), 0)

    def test_mixed_numbers(self):
        """Tests a list containing both even and odd numbers."""
        self.assertEqual(count_even_numbers([1, 2, 3, 4, 'five', 6.0]), 2)

    def test_negative_even_numbers(self):
        """Tests a list containing negative even numbers."""
        self.assertEqual(count_even_numbers([-2, -4, 'a', -8]), 3)

    def test_empty_list(self):
        """Tests an empty list."""
        self.assertEqual(count_even_numbers([]), 0)

    def test_non_integer_elements(self):
        """Tests a list with various non-integer elements."""
        self.assertEqual(count_even_numbers([1, 'two', 3.5, None, True, 4]), 1)

    def test_boundary_case_single_even(self):
        """Tests a list with a single even number."""
        self.assertEqual(count_even_numbers([2]), 1)

    def test_boundary_case_single_odd(self):
        """Tests a list with a single odd number."""
        self.assertEqual(count_even_numbers([1]), 0)

