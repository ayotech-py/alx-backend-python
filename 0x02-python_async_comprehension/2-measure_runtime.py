#!/usr/bin/env python3

import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    start = asyncio.get_running_loop().time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())

    end = asyncio.get_running_loop().time()
    return end - start
