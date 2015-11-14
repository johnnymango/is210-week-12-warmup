#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """This is the error handling for ages."""
    pass


def get_age(birthyear):
    """This function returns an age based on birthyear.

    Args:
        birthyear (int):  Interger representing birth year.

    Returns:
        Int: The age.

    Examples:
        >>> get_age(1977)
        38

    Raises:
        InvalidAgeError: if birthyear is greater than the curreny year.


    """
    if birthyear > datetime.datetime.now().year:
        raise InvalidAgeError('This is an invalid birthyear.')
    else:
        age = datetime.datetime.now().year - birthyear
        return age
