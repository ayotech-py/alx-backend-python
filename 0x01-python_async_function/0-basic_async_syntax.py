#!/usr/bin/env python3

import time
import random


async def wait_random(max_delay=10) -> float:
    random_time = random.randint(max_delay + 1)
    await time.sleep(random_time)
    return random_time
