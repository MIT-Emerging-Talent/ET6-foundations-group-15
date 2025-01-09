#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the `count_evens` function.
"""

import unittest
from solutions.count_even_numbers import count_evens


class TestCountEvens(unittest.TestCase):
    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(count_evens([]), 0)

    def test_no_even_numbers(self):
        """Test with a list containing no even numbers."""
        self.assertEqual(count_evens([1, 3, 5]), 0)

    def test_all_even_numbers(self):
        """Test with a list containing only even numbers."""
        self.assertEqual(count_evens([2, 4, 6, 8]), 4)

    def test_mixed_numbers(self):
        """Test with a list containing mixed numbers and types."""
        self.assertEqual(count_evens([1, 2, "a", None, 4, 6]), 3)

    def test_non_integer_elements(self):
        """Test with a list containing non-integer elements."""
        self.assertEqual(count_evens(["hello", None, 3.14, [], {}]), 0)

    def test_type_error(self):
        """Test with an input that is not a list."""
        with self.assertRaises(TypeError):
            count_evens("not a list")
