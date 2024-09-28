#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/split-array-largest-sum/description/?envType=problem-list-v2&envId=prefix-sum
# ============================================================

"""
给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组。

设计一个算法使得这 k 个子数组各自和的最大值最小。
"""
import bisect
import itertools
import math
from typing import List


class Solution:
    """
    nums元素非负，即子数组每增加一个元素，对应的子数组和必然大于等于增加前的子数组和。

    任给定一个整数x，将nums拆分成多个子数组，要求每个子数组的和小于等于x，
    假定这个时候拆分的子数组有y个。那么
        - y > k: 增加x，那么y会变小
        - y = k: 减小x以找到最小的y
        - y < k: 减小x，那么y会变大
    尝试二分搜索x即可。x的区域为[max(nums), sum(nums)]。
    """

    def splitArray(self, nums: List[int], k: int) -> int:
        def check(x: int):
            counter = 0
            s = 0
            for v in nums:
                s += v
                if s > x:
                    counter += 1
                    if counter >= k:
                        return False
                    s = v
            return counter + 1 <= k

        start = max(nums)
        index = bisect.bisect_left(range(start, sum(nums) + 1), True, key=check)
        return start + index


class Solution2:
    """
    动态规划。
    令dp[i][j]表示nums前nums[0:i]划分成j个子数组的情况下，所有子数组和的最小值。
        dp[i][j] = min{
            max{dp[k][j-1], sums(nums[k+1:i])} for all k < i
        }

    """

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        prefix_sums = [0]
        prefix_sums.extend(itertools.accumulate(nums))

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for t in range(0, i):
                    dp[i][j] = min(max(dp[t][j - 1], prefix_sums[i] - prefix_sums[t]), dp[i][j])
        return dp[n][k]


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([7, 2, 5, 10, 8], 2), 18),
        (([1, 2, 3, 4, 5], 2), 9),
        (([1, 4, 4], 3), 4)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().splitArray(*case_input)}')
