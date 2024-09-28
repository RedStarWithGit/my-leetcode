#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/best-sightseeing-pair/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

返回一对观光景点能取得的最高分。
"""

from typing import List


class Solution:
    """
    values[i] + values[j] + i - j = (values[i] + i) + (values[j] - j)

    枚举j，取j之前最大的values[i] + i相加，最大值即可
    """

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        result = 0
        i_value = values[0] + 0
        for j in range(1, n):
            result = max(result, i_value + (values[j] - j))
            i_value = max(i_value, values[j] + j)
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([8, 1, 5, 2, 6], 11),
        ([1, 2], 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxScoreSightseeingPair(case_input)}')
