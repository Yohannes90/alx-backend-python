#!/usr/bin/env python3
''' from wait_n and alter it into a new function task_wait_n
    identical to wait_n except task_wait_random is being called.
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Asynchronously waits for a random delay n times
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
