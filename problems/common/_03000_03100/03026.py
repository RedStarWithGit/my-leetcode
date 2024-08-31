#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-good-subarray-sum/description/
# ============================================================
"""
给你一个长度为 n 的数组 nums 和一个 正 整数 k 。

如果 nums 的一个子数组中，第一个元素和最后一个元素 差的绝对值恰好 为 k ，我们称这个子数组为 好 的。
换句话说，如果子数组 nums[i..j] 满足 |nums[i] - nums[j]| == k ，那么它是一个好子数组。

请你返回 nums 中 好 子数组的 最大 和，如果没有好子数组，返回 0 。
"""
import math
from typing import List


class Solution:
    """
    首先构造前缀和数组s，其中sums[i+1] = nums[0] + nums[1] + ... + nums[i]
        所以nums[i..j]的和为sums[j+1] - sums[i]。

    之后需要确定子数组nums[i:j+1]中的i和j：
        - 遍历j
        - 从已遍历的nums中找到nums[i] == nums[j] + k 或 nums[i] == nums[j] - k的i
            - 由于需要令sums[j+1] - sums[i]最大，我们只需要保证有一个最小的sums[i]即可
            - 维护一个nums[i] => 最小的sums[i]的dict
    """

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = [0] * (n + 1)
        for i, v in enumerate(nums):
            sums[i + 1] = sums[i] + nums[i]

        found = False
        min_sums = {}
        result = -math.inf

        for j, value in enumerate(nums):
            for other in (value - k, value + k):
                if other in min_sums:
                    found = True
                    result = max(sums[j + 1] - min_sums[other], result)

            if value not in min_sums:
                min_sums[value] = sums[j]
            else:
                min_sums[value] = min(sums[j], min_sums[value])

        return result if found else 0


class Solution2:
    """
    参考题解：
    并不需要一开始就计算出前缀和数组，min_sums维护的是已访问的nums的前缀和，在遍历j的过程中计算即可，
    """

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        found = False
        min_sums = {}
        result = -math.inf
        sums = 0
        for j, value in enumerate(nums):
            sums += value
            for other in (value - k, value + k):
                if other in min_sums:
                    found = True
                    result = max(sums - min_sums[other], result)

            if value not in min_sums:
                min_sums[value] = sums - value
            else:
                min_sums[value] = min(sums - value, min_sums[value])

        return result if found else 0


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (([1, 2, 3, 4, 5, 6], 1), 11),
        (([-1, 3, 2, 4, 5], 3), 11),
        (([-1, -2, -3, -4], 2), -6),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().maximumSubarraySum(*i)}')
