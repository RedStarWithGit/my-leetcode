#!/usr/bin/env python
# coding=utf-8
# ============================================================
# Author: ChenBing
# ============================================================
# read cases' input
# ============================================================

import os.path
from typing import Callable
from typing import List


def _as_int_list(line: str) -> List[int]:
    if not line.startswith('[') or not line.endswith(']'):
        raise Exception(f"line is not a list: {line}")

    return [int(each) for each in line[1:-1].split(',')]


def _as_int_list_list(line: str) -> List[List[int]]:
    if not line.startswith('[') or not line.endswith(']'):
        raise Exception(f"line is not a list of int: {line}")

    results = []
    start = 1
    while True:
        end = line.find(']', start)
        if end < 0:
            break

        results.append([int(each) for each in line[start + 1:end].split(',')])
        start = line.find('[', end + 1)
        if start < 0:
            break

    return results


def _read_case_input_from_filepath(filepath: str, converter: List[Callable[[str], object]]) -> List:
    if not filepath:
        raise Exception(f"filepath cannot be null or empty")

    if not os.path.isfile(filepath):
        raise Exception(f"there is no case input filepath on {filepath}")

    case_inputs = []

    converter_len = len(converter)
    index = 0
    with open(filepath, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            case_inputs.append(converter[index](line))
            index = (index + 1) % converter_len
    return case_inputs
