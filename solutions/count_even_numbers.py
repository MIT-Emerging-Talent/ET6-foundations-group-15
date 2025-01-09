#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines the function `count_evens`  
to count the number of even numbers in a list.  
It handles cases where non-integer elements are ignored.

Author: Norbert Ndayisenga
Date: 07 01 2024
"""


def count_evens(numbers: list) -> int:
    """
    Counts the number of even integers in a given list.

    Parameters:
        numbers (list): The input list to evaluate.

    Returns:
        int: The number of even integers in the input list.

    Examples:
        >>> count_evens([1, 2, 3, 4])
        2
        >>> count_evens([1, 'a', None, 2.5])
        0
        >>> count_evens([2, 4, 6])
        3
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    return sum(1 for num in numbers if isinstance(num, int) and num % 2 == 0)
