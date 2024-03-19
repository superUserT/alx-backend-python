#!/usr/bin/env python3
"""
    this module meassures the avarage time it takes for a routine to run
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measure_time:
            measure the time it takes to run a concurrent routine

        Args:
            n (int): number of routines
            max_delay (int): maximum delay

        Returns:
            float: average time elapsed
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
