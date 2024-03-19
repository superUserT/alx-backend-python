#!/usr/bin/env python3
"""
    an asynchrounous coroutine
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        wait_random:
            wait a random amount of time

        Args:
            float: a reandom float number
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
