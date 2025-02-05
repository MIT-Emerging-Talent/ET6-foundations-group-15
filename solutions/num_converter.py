#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting binary into decimal and vice versa.

Module contents:
    - decimal_to_binary: converts a non-negative decimal number into its binary representation.
    - binary_to_decimal: converts a binary number into its decimal representation.

Created on 31 12 24
@author: Abdallah Alnajjar
"""


def decimal_to_binary(decimal: int) -> int:
    """
    Converts a decimal number to its binary representation

    Parameters:
        decimal_number (int): The decimal number (non-negative integer) to be converted.

    Returns:
        int: The binary representation of the input decimal number.

    Raises:
    AssertionError: If the input is not an integer.
    AssertionError: If the decimal is a negative number.

    >>> decimal_to_binary(254)
    11111110
    >>> decimal_to_binary(13)
    1101
    >>> decimal_to_binary(173)
    10101101

    """

    # validate input type
    assert isinstance(decimal, int), "Input must be an integer"

    # ensure that the decimal is positive
    assert decimal >= 0

    # Handle the special case where decimal is 0
    if decimal == 0:
        return 0

    binary_list = []
    binary_num = ""

    # Convert decimal to binary digits
    while decimal != 0:
        if decimal % 2 == 1:
            binary_list.append(1)
            decimal -= 1
        elif decimal % 2 == 0:
            binary_list.append(0)
        decimal = decimal / 2

    # Form the final binary representation
    for num in reversed(binary_list):
        binary_num = binary_num + str(num)
    return int(binary_num)


def binary_to_decimal(binary: int) -> int:
    """
    Converts a binary number (as an integer) to its decimal representation.

    Parameters:
        binary (int): The binary number to be converted.

    Returns:
        int: The decimal equivalent of the binary number.

    Raises:
    AssertionError: If the input is not an integer.
    AssertionError: If the input contains digits other than 1 or 0.

    >>> binary_to_decimal(10110101)
    181
    >>> binary_to_decimal(1010101)
    85
    >>> binary_to_decimal(11111)
    31
    """
    # validate input type
    assert isinstance(binary, int), "Input must be an integer"

    # Ensure the input is treated as a string
    binary = str(binary)
    decimal = 0

    # ensure that the input contains only zeros and ones
    assert all(char in "01" for char in binary)

    # Start writing the binary representation.
    for bit in binary:
        decimal += (2 ** (len(binary) - 1)) * int(bit)
        binary = binary[1:]

    return decimal
