#!/usr/bin/env python3
"""Module for async_comprehension coroutine"""

from typing import List
from async_generator_0 import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from an asynchronous generator.

    Returns:
        List[float]: A list of 10 float values between 0 and 10.
    """
    return [i async for i in async_generator()]
