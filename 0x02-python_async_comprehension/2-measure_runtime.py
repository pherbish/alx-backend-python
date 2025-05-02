#!/usr/bin/env python3
"""Module for measuring execution time of async_comprehension run in parallel."""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures total runtime of running async_comprehension 4 times in parallel.

    Returns:
        float: Total execution time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
