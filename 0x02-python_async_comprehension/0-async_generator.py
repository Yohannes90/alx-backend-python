#!/usr/bin/env python3
''' function that asynchronously yield a random number between 0 and 10
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' asynchronously yield a random number between 0 and 10 in 1 sec
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
