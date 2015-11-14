#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """This function returns a simple index.

    Args:
        var1 (mixed): A variable.
        var2 (mixed): A variable.

    Returns:
        Mixed:  The index/key.

    Examples:
        >>> simple_lookup([1, 2, 3, 4], 2)
        3

        >>> simple_lookup([1,2], 4)
        Warning: Your index/key does not exist.
        [1, 2]
    """
    try:
        return var1[var2]
    except LookupError:
        print 'Warning: Your index/key does not exist.'
        return var1
