#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for checking if a number is a perfect square.

Module contents:
    - is_perfect_square: checks if a given number is a perfect square.

Created on 2025-01-10
@author: Huda Alamassi
"""

from typing import Union


def is_perfect_square(num: Union[int, float]) -> bool:
    """
    The function takes a number (integer or float) and checks if it is a perfect square.

    A perfect square is a number whose square root is an integer.

    Arguments:
    num (int, float): The number to be checked.
        - Assumed that the number is either an integer or a float.

    Returns:
    bool:
        - True if the number is a perfect square, False otherwise.

    Raises:
    AssertionError: If the input is not a number (either int or float).

    Examples:
        >>> is_perfect_square(16)
        True

        >>> is_perfect_square(14)
        False

        >>> is_perfect_square(25.0)
        True

        >>> is_perfect_square(0.0)
        True

        >>> is_perfect_square(14.5)
        False
    """
    # Validate the input
    assert isinstance(num, (int, float)), "Input must be a number (int or float)"

    if num < 0:
        return False

    sqrt = num**0.5

    sqrt_int = int(sqrt)

    squared = sqrt_int * sqrt_int

    return squared == num
