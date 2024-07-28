#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/single-number/description/
# ============================================================

"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
"""
from typing import List


class Solution:
    """
    x ^ x = 0
    x ^ 0 = x
    """

    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            r = 0
            for x in nums:
                r = r ^ x
            return r


if __name__ == '__main__':
    # 过于简单直接提交
    solution = Solution

    for idx, (i, o) in enumerate([

    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
