#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/smallest-range-i/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个整数数组 nums，和一个整数 k 。

在一个操作中，您可以选择 0 <= i < nums.length 的任何索引 i 。
将 nums[i] 改为 nums[i] + x ，其中 x 是一个范围为 [-k, k]
的任意整数。对于每个索引 i ，最多 只能 应用 一次 此操作。

nums 的 分数 是 nums 中最大和最小元素的差值。

在对  nums 中的每个索引最多应用一次上述操作后，返回 nums 的最低 分数 。
"""

from typing import List


class Solution:
    """
    原来的差值是max - min，经过二次变化，max和min都向彼此靠近。
    """

    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        diff -= k * 2
        if diff < 0:
            return 0
        return diff


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([1], 0), 0),
        (([0, 10], 2), 6),
        (([1, 3, 6], 3), 0)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().smallestRangeI(*case_input)}')
