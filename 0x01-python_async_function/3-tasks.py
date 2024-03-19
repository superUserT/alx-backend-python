#!/usr/bin/env python3
"""
    this module returns an async task
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        task_wait_random:
            returns a asyncio task

        Args:
            max_delay (int): maximum delay

        Returns:
            asyncio.Task: the task object
    """

    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
