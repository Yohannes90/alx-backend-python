#!/usr/bin/env python3
''' function that waits for random delay between 0 and max_delay
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' takes an int arg wait_random then wait for a random delay before return
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()

    return delays
