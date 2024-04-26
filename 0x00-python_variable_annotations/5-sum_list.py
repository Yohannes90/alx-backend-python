#!/usr/bin/env python3
''' function that adds a list of floats
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' takes a list of floats as arguments and returns their sum as a float
    '''
    sum = 0
    for i in input_list:
        sum += i
    return sum
