#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-number-of-good-pairs-i/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你两个整数数组 nums1 和 nums2，长度分别为 n 和 m。同时给你一个正整数 k。

如果 nums1[i] 可以除尽 nums2[j] * k，则称数对 (i, j) 为 优质数对（0 <= i <= n - 1, 0 <= j <= m - 1）。

返回 优质数对 的总数。
"""
import itertools
from typing import List


class Solution:
    """
    数量级为1 <= nums1[i], nums2[j] <= 50，枚举即可
    """

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for x, y in itertools.product(nums1, nums2):
            if x % (y * k) == 0:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([1, 3, 4], [1, 3, 4], 1), 5),
        (([1, 2, 4, 12], [2, 4], 3), 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().numberOfPairs(*case_input)}')
