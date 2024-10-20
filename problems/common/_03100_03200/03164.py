#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你两个整数数组 nums1 和 nums2，长度分别为 n 和 m。同时给你一个正整数 k。

如果 nums1[i] 可以被 nums2[j] * k 整除，则称数对 (i, j) 为 优质数对（0 <= i <= n - 1, 0 <= j <= m - 1）。

返回 优质数对 的总数。
"""
from collections import Counter
from typing import List


class Solution:
    """
    同3162，数量级增加：
        - 1 <= n, m <= 10^5
        - 1 <= nums1[i], nums2[j] <= 10^6

    先统计nums各数字的出现次数
        O(n) + O(m)
    再遍历nums2[j]，针对每一个j，再遍历nums2[j] * k的1~x倍，其中x=max(nums1) // (nums2[j] * k)
    """

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counter1 = Counter(nums1)
        max_nums1_value = max(nums1)
        counter2 = Counter(nums2)

        result = 0
        for num, times in counter2.items():
            target = num * k
            for i in range(1, max_nums1_value // target + 1):
                if target * i in counter1:
                    result += counter1[target * i] * times
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([1, 3, 4], [1, 3, 4], 1), 5),
        (([1, 2, 4, 12], [2, 4], 3), 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().numberOfPairs(*case_input)}')
