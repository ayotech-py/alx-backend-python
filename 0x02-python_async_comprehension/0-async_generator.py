#!/usr/env/bin python3

import random
import asyncio


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
