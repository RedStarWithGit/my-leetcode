#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""
from typing import List


class Solution:
    """
    平方数 >= 0，原数组中按绝对值排序，小的平方放前面。
    由于nums以排序，用栈存储负数，择机出栈。
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        results = []
        vector = []
        for v in nums:
            if v < 0:
                vector.append(-v)
            elif v == 0:
                results.append(v ** 2)
            else:
                while vector and vector[-1] <= v:
                    results.append(vector.pop() ** 2)
                results.append(v ** 2)
        while vector:
            results.append(vector.pop() ** 2)
        return results


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().sortedSquares(case_input)}')
