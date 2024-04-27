#!/usr/bin/env python3
''' function that adds floats
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' takes list lst as argument and return first element if list not empty
    '''
    if lst:
        return lst[0]
    else:
        return None
