#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
你有一个初始为空的浮点数数组 averages。另给你一个包含 n 个整数的数组 nums，其中 n 为偶数。

你需要重复以下步骤 n / 2 次：
- 从 nums 中移除 最小 的元素 minElement 和 最大 的元素 maxElement。
- 将 (minElement + maxElement) / 2 加入到 averages 中。

返回 averages 中的 最小 元素。
"""

from typing import List


class Solution:
    """
    nums排序后遍历
    """

    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        min_value = (nums[0] + nums[-1]) / 2
        for i in range(1, n // 2):
            min_value = min(min_value, (nums[i] + nums[-i - 1]) / 2)
        return min_value


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([7, 8, 3, 4, 15, 13, 4, 1], 5.5),
        ([1, 9, 8, 3, 10, 5], 5.5),
        ([1, 2, 3, 7, 8, 9], 5.0)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().minimumAverage(case_input)}')
