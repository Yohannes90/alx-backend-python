#!/usr/bin/env python3
''' function that return zoomed list
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' takes a tuple and optional factor, return list repeating
        each element by factor times
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
