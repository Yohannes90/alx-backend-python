#!/usr/bin/env python3
''' function that return length of list of sequence
'''
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' return length of list of sequence
    '''
    return [(i, len(i)) for i in lst]
