#!/usr/bin/env python3
from typing import Callable
"""
returns a function that
multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a multipled float
    """
    def mult_func(n: float) -> float:
        """
        returns a value multiplied by (multiplier)
        """
        return n * multiplier
    return mult_func
