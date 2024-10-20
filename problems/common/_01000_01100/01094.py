#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/car-pooling/description/
# ============================================================

"""
车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）

给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi]
表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。
这些位置是从汽车的初始位置向东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
"""

import bisect
from collections import Counter
from typing import List


class Solution:
    """
    (number, from, to)：from位置上车，to位置下车，可以将(number, from, to)转换为：
        - (from, number)
        - (to, -number)
    按from/to升序排序。
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        values = []
        for t in trips:
            bisect.insort_left(values, (t[1], t[0]))
            bisect.insort_left(values, (t[2], -t[0]))

        passengers = 0
        for _, number in values:
            passengers += number
            if passengers > capacity:
                return False
        return True


class Solution2:
    """
    from增加，to减少，统计所有position的人员变化
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counter = Counter()
        for number, from_, to_ in trips:
            counter[from_] += number
            counter[to_] -= number

        value = 0
        for k in sorted(counter):
            value += counter[k]
            if value > capacity:
                return False
        return True


class Solution3:
    """
    官方题解：差分数组

    from/to取值都满足：0 <= from < to <= 1000
    """

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diffs = [0] * 1001
        for number, from_, to_ in trips:
            diffs[from_] += number
            diffs[to_] -= number

        value = 0
        for v in diffs:
            value += v
            if value > capacity:
                return False
        return True


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([[2, 1, 5], [3, 3, 7]], 4), False),
        (([[2, 1, 5], [3, 3, 7]], 5), True),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().carPooling(*case_input)}')
