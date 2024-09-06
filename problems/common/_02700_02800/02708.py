#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-strength-of-a-group/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。
老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的
学生下标为 i0, i1, i2, ... , ik ，那么这个小组的实力值定义为
nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​] 。

请你返回老师创建的小组能得到的最大实力值为多少。
"""
import math
from typing import List


class Solution:
    """
    题设数据范围如下：
        1 <= nums.length <= 13
        -9 <= nums[i] <= 9

    显然，尽可能取所有的正数，之后尽可能地取偶数个负数且负数尽可能小
    """

    def maxStrength(self, nums: List[int]) -> int:
        result = 1

        nums.sort()
        n = len(nums)
        neg = False
        selected = False
        for i, e in enumerate(nums):
            if e > 0:
                result *= e
                selected = True
            elif e < 0:
                if neg:
                    result *= e
                    neg = False
                    selected = True
                elif i < n - 1 and nums[i + 1] < 0:
                    result *= e
                    neg = True
                    selected = True
        return result if selected else nums[-1]


class Solution2:
    """
    题设数据范围如下：
        1 <= nums.length <= 13
        -9 <= nums[i] <= 9

    不排序。
    所有非0的数相乘，若<0则除去最大的负数，若没选择数字则返回最大的元素
    """

    def maxStrength(self, nums: List[int]) -> int:
        result = 1
        max_element = nums[0]
        max_negative = -math.inf
        selected = 0
        for e in nums:
            if e != 0:
                result *= e
                selected += 1
            max_element = max(max_element, e)
            if e < 0:
                max_negative = max(max_negative, e)
        if result < 0:
            result = result // max_negative
            selected -= 1
        if selected == 0:
            return max_element
        return result


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([3, -1, -5, 2, 5, -9], 1350),
        ([-4, -5, -4], 20),
        ([0, -1], 0)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxStrength(case_input)}')
