#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个二进制数组 nums 。

你可以对数组执行以下操作 任意 次（也可以 0 次）：

选择数组中 任意 一个下标 i ，并将从下标 i 开始一直到数组末尾 所有 元素 反转 。
反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。

请你返回将 nums 中所有元素变为 1 的 最少 操作次数
"""

from typing import List


class Solution:
    """
    模拟，但不能真的对i后面所有的数做一次反转操作，否则最坏场景可能为O(n^2)，题设数据量会超时。

    反转奇数次是^1，反转偶数次是本身，可以统计之前需要执行的反转次数。
    """

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        reverse_counter = 0
        for e in nums:
            if e == reverse_counter:
                result += 1
                reverse_counter = (reverse_counter + 1) % 2
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([0, 1, 1, 0, 1], 4),
        ([1, 0, 0, 0], 1),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().minOperations(case_input)}')
