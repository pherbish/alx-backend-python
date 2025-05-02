#!/usr/bin/env python3
"""Module for async_generator coroutine."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield 10 random float numbers between 0 and 10.

    Each number is yielded after a 1-second asynchronous wait.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
