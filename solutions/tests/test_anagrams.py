"""
A module for testing the are_anagrams function.

Tests included:
    - When two words are anagarms
    - When two words are not anagrams
    - When the input is two phrases, not words
    - When the input is not a string

Created on 04 01 24
@author: Abdallah Alnajjar
"""

import unittest

from ..anagrams import are_anagrams


class TestAnagrams(unittest.TestCase):
    """
    Tests the function "are_anagrams" in the file anagarms.
    """

    def test_anagrams_two_correct_words(self):
        """
        It should return True if Earth and Heart are anagrams
        """
        actual = are_anagrams("Earth ", "Heart")
        self.assertEqual(actual, True)

    def test_anagrams_two_incorrect_words(self):
        """
        It should return False since David and Aboodi are not anagrams
        """
        actual = are_anagrams("David", "Aboodi")
        self.assertEqual(actual, False)

    def test_anagrams_phrases(self):
        """
        It should return True as the two phrases are anagrams
        """
        actual = are_anagrams("I am not active", "Vacation time")
        self.assertEqual(actual, True)

    def test_anagrams_integer(self):
        """
        It should raise an assertion error if one of the inputs
        is not a string
        """
        with self.assertRaises(AssertionError):
            are_anagrams(20105140, 4351315)
