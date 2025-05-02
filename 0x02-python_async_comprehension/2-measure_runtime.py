import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime():
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
