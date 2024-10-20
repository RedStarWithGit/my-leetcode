#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个数组 nums ，数组中的数字 要么 出现一次，要么 出现两次。

请你返回数组中所有出现两次数字的按位 XOR 值，如果没有数字出现过两次，返回 0 。
"""

from typing import List


class Solution:
    """
    1 <= nums[i] <= 50
    """

    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = [0] * 51
        for v in nums:
            counts[v] += 1
        result = 0
        for index, value in enumerate(counts):
            if value == 2:
                result = result ^ index
        return result


class Solution2:
    """
    参考题解：使用O(1)空间
    由于1 <= nums[i] <= 50，可以使用一个50位的二进制来表示某个数是否出现
    """

    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        visit = 0
        result = 0
        for v in nums:
            if ((visit >> v) & 1) == 1:
                result = result ^ v
            else:
                visit = visit | (1 << v)
        return result


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([1, 2, 1, 3], 1),
        ([1, 2, 3], 0),
        ([1, 2, 2, 1], 3),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().duplicateNumbersXOR(case_input)}')
