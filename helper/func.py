#!/usr/bin/env python
# coding=utf-8
# ============================================================
# Author: ChenBing
# ============================================================
import functools
import time

from typing import Callable


def func_cost_wrapper(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'function {func.__name__} execution has spent {end - start}s')
        return result

    return wrapper
