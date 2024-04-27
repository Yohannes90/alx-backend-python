#!/usr/bin/env python3
''' function that return given element from a dict
'''


from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')
M = Mapping
A = Any
U = Union


def safely_get_value(dct: M, key: A, default: U[T, None] = None) -> U[Any, T]:
    ''' takes dict and key as argument and return given element
    '''
    if key in dct:
        return dct[key]
    else:
        return default
