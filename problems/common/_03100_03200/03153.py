#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/description/?envType=daily-question&envId=2024-08-27
# ============================================================

"""
你有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。

两个整数的 数位差 指的是两个整数 相同 位置上不同数字的数目。

请你返回 nums 中 所有 整数对里，数位差之和。
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    相同数位的值不同则+1。

    任意数位上可用的取值为[0, 9]。
    假定整个nums中第一位上各数字出现的次数为Xi，即0出现了x0次，1出现了x1次，……，9出现了x9次。
    0之外的数有x1+x2+x3+x4+x5+x6+x7+x8+x9（即n-x0）个，即每个0有n - x0不同的值，则0总共有x0 * (n - x0)个。
    对1-9重复该逻辑。
    遍历所有数位相加。
    """

    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        while nums[0] > 0:
            counter = defaultdict(int)
            for i in range(n):
                counter[nums[i] % 10] += 1
                nums[i] = nums[i] // 10

            total = 0
            for bit in range(0, 10):
                total += counter[bit] * (n - counter[bit])
            result += total // 2
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([13, 23, 12], 4),
        ([10, 10, 10, 10], 0)
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().sumDigitDifferences(i)}')
