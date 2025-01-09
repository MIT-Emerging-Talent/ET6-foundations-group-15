#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the function `count_evens` to count the number of even numbers
in a given list of elements. The function handles mixed types and counts even numbers
without excluding the entire list if it contains non-integers.

Author: Norbert Ndayisenga
Date: 07 01 2024
"""

def count_evens(numbers: list) -> int:
    """
    Counts the number of even integers in a given list.

    Parameters:
        numbers (list): The input list of elements to evaluate.

    Returns:
        int: The number of even integers in the input list.

    Raises:
        TypeError: If the input is not a list.

    Examples:
        >>> count_evens([1, 2, 3, 4, 5, 6])
        3
        >>> count_evens([])
        0
        >>> count_evens([-2, -4, 3, 5, "string", None])
        2
    """
    # Ensure the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Count even integers
    even_count = 0
    for item in numbers:
        if isinstance(item, int) and item % 2 == 0:
            even_count += 1

    return even_count
