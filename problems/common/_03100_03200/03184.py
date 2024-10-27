#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-i/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j
且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。

整天 定义为时间持续时间是 24 小时的 整数倍 。
例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。
"""

import itertools
from collections import defaultdict
from typing import List


class Solution:
    """
    数量级较小，遍历
    """

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for x, y in itertools.combinations(hours, 2):
            if (x + y) % 24 == 0:
                count += 1
        return count


class Solution2:
    """
    (x + y) % 24 == 0，若x、y都小于24，那么在确定x的情况下：
        - 若x = 0，则y = 0
        - 若x > 0，则y = 24 - x
    """

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        result = 0
        counter = defaultdict(int)
        for h in hours:
            h = h % 24
            result += counter[0 if h == 0 else 24 - h]
            counter[h] += 1
        return result


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([12, 12, 30, 24, 24], 2),
        ([72, 48, 24, 3], 3)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().countCompleteDayPairs(case_input)}')
