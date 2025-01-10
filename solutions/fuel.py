"""
This module provides functionality to convert a fraction to
a percentage and display it in a user-friendly format.

Functions:
    main(): Entry point of the program that handles user input and output.
    convert(fraction): Converts a fraction string (e.g., '1/2') into a percentage.
    gauge(percentage): Converts a percentage into a user-friendly string representation.

Author: Alnajjar
Date: 10 01 2025
"""


def main():
    """
    Continuously prompts the user for a fraction input, converts it
    to a percentage, and displays the result.
    """
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except AssertionError as e:
            print(e)


def convert(fraction):
    """
    Converts a fraction string into a percentage.

    Args:
        fraction (str): A string representing a fraction in the format 'X/Y'.

    Returns:
        int: The percentage equivalent of the fraction, rounded to the nearest integer.

    Raises:
        AssertionError: If the numerator is greater than the denominator,
        or if the input is invalid.

    Examples:
        >>> convert("1/2")
        50
        >>> convert("3/4")
        75
        >>> convert("2/5")
        40
    """
    x, y = fraction.split("/")

    # Assert that both parts of the fraction are digits
    assert (
        x.isdigit() and y.isdigit()
    ), "Both numerator and denominator must be integers."

    x, y = int(x), int(y)

    assert y != 0, "Denominator cannot be zero."

    assert x >= 0 and y > 0, "Numerator and denominator must be non-negative."

    assert x <= y, "Numerator cannot be greater than denominator."

    return round((x / y) * 100)


def gauge(percentage):
    """
    Converts a percentage into a user-friendly string representation.

    Args:
        percentage (int): An integer representing a percentage (0-100).

    Returns:
        str: 'F' if the percentage is greater than 99, 'E' if less than 1,
        otherwise the percentage followed by '%'.

    Raises:
        AssertionError: If the percentage is not within the range 0-100.

    Examples:
        >>> gauge(50)
        '50%'
        >>> gauge(100)
        'F'
        >>> gauge(0)
        'E'
    """
    # Assert that percentage is within valid range
    assert 0 <= percentage <= 100, "Percentage must be between 0 and 100."

    if percentage > 99:
        return "F"
    elif percentage < 1:
        return "E"
    else:
        return f"{percentage}%"
