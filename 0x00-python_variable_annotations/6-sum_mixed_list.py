#!/usr/bin/env python3
''' function that adds a list of floats and integers
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    ''' takes a list of floats as arguments and returns their sum as a float
    '''
    sum = 0
    for i in mxd_list:
        sum += i
    return sum
