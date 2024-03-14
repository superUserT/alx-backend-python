#!/usr/bin/env python3
from typing import Iterable, Tuple, Sequence, List
"""
returns list of a list
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuple
    """
    return [(i, len(i)) for i in lst]
