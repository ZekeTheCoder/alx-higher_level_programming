#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Adds two integers.

    :param a: An integer or float.
    :param b: An integer or float (default is 98).

    :return: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float..
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
