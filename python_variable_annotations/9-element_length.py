#!/usr/bin/env python3

""" Module for element_length function """


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a list of tuples with the length
  of each element in the input list """
    return [(i, len(i)) for i in lst]
