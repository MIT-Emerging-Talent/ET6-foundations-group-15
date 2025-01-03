#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking whether two strings are anagrams.

Module contents:
    - are_anagrams: takes 2 strings as arguments and check whether they are anagrams.

Created on 03 01 25
@author: Abdallah Alnajjar
"""


def are_anagrams(word_1: str, word_2: str):
    """
    Checks whether two strings are anagrams.

    Parameters:
        word_1 (str): The first word (string) to be compared.
        word_2 (str): The second word (string) to be compared.

    Returns:
        bool: "True" if the two string are anagrams,
        and "False" if it's not the case

    Raises:
    AssertionError: If the input is not a string.

    >>> binary_to_decimal(254)
    11111110
    >>> binary_to_decimal(13)
    1101
    >>> binary_to_decimal(173)
    10101101

    """

    # Remove spaces and convert to lowercase for accurate comparison
    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()

    # Check if sorted characters of both strings are equal
    return sorted(word_1) == sorted(word_2)
