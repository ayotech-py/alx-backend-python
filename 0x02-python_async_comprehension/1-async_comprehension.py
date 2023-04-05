#!/usr/bin/env python3

import random
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    async for num in async_generator():
        random_nums.append(num)
    return random_nums
