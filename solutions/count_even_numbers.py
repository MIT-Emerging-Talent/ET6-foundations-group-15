#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting even numbers in a given list.

Module contents:
- count_even_numbers: Counts the even integers in a list while ignoring non-integer elements.

Created on January 8, 2025

@author: Norbert Ndayisenga
"""

from typing import List


def count_even_numbers(numbers: List) -> int:
    """
    Count the even integers in a list while ignoring non-integer elements.

    Args:
        numbers (List): A list of elements of any type.

    Returns:
        int: The count of even integers in the list.

    Examples:
        >>> count_even_numbers([2, 4, 6, 8])
        4
        >>> count_even_numbers([1, 3, 5, 7])
        0
        >>> count_even_numbers([1, 2, 3, 4, 'five', 6.0])
        2
        >>> count_even_numbers([-2, -4, 'a', -8])
        3
        >>> count_even_numbers([])  # An empty list should return 0
        0
    """
    even_count = 0
    for num in numbers:
        if isinstance(num, int) and num % 2 == 0:
            even_count += 1
    return even_count
