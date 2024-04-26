#!/usr/bin/env python3
''' function that multiplies a float by multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' returns function that multiplies a float by argument multiplier
    '''
    return lambda x: x * multiplier
