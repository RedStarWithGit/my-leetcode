#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/smallest-range-ii/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个整数数组 nums，和一个整数 k 。
对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。
nums 的 分数 是 nums 中最大元素和最小元素的差值。
在更改每个下标对应的值之后，返回 nums 的最小 分数 。
"""

from typing import List


class Solution:
    """
    nums排序，那么差值为nums[n-1] - nums[0]。
    任取 i < j，有如下几种变化：
        - (+, +)：差值不变
        - (-, -)：差值不变
        - (+, -)：nums[i]和nums[j]靠拢，差值变为abs((nums[j] - k) - (nums[i] + k)) = abs(nums[j] - nums[i] - 2*k)
        - (-, -)：nums[i]和nums[j]远离，差值变为abs((nums[j] + k) - (nums[i] - k)) = abs(nums[j] - nums[i] + 2*k)
    显然，(+, -)的差值会小于(-, +)的差值，即只需要选择(+, -)变化即可。

    任取i，对nums[0..i]做+k操作，对nums[i+1..n-1]做-k操作，操作后：
        最大值为max(nums[i] + k, nums[n-1] - k)
        最小值为min(nums[0] + k, nums[i+1] - k)
    i从0到n-2遍历即可。
    """

    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        nums.sort()
        value = nums[-1] - nums[0]
        if k == 0:
            return value

        for i in range(n - 1):
            min_value = min(nums[0] + k, nums[i + 1] - k)
            max_value = max(nums[i] + k, nums[-1] - k)
            value = min(value, max_value - min_value)
        return value


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([2, 7, 2], 1), 3),
        (([1], 0), 0),
        (([0, 10], 2), 6),
        (([1, 3, 6], 3), 3)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().smallestRangeII(*case_input)}')
