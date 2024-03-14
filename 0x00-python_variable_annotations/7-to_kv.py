#!/usr/bin/env python3
from typing import Union, Tuple
"""
returns a tuple of a string and number
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a key, value tuple
    """
    return k, v ** 2
