#!/usr/bin/env python3
""" TASK 1 """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ pagination program """
    tupla: Tuple[int, int] = (page * page_size - page_size, page * page_size)
    return tupla
