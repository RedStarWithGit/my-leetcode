#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个正整数数组 nums 。
- 元素和 是 nums 中的所有元素相加求和。
- 数字和 是 nums 中每一个元素的每一数位（重复数位需多次求和）相加求和。
返回 元素和 与 数字和 的绝对差。
注意：两个整数 x 和 y 的绝对差定义为 |x - y| 。
"""

from typing import List


class Solution:
    """
    正整数数组，每个元素>0。

    假设 a>0，b>0，c>0
        x = a*10^2 + b*10 + c
        y = a + b + c
    显然x >= y。
    显然nums的每个元素其本身都会大于其数字和。
    """

    def differenceOfSum(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            y = x
            while y > 0:
                x -= (y % 10)
                y = y // 10
            result += x
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([1, 15, 6, 3], 9),
        ([1, 2, 3, 4], 0),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().differenceOfSum(case_input)}')
