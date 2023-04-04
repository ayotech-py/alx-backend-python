#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    random_time = random.randint(max_delay + 1)
    await asyncio.sleep(random_time)
    return random_time
