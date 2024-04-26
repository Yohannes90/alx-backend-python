#!/usr/bin/env python3
''' function that returns a tuple where second element is square of int/float v
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' takes a string k and an int OR float v as arguments and returns a tuple
    '''
    return (k, float(v**2))
