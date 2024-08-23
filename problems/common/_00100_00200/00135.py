#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/candy/description/
# ============================================================

"""
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
"""

from typing import List


class Solution:
    """
    向左遍历，若
        - ratings[i] < ratings[i+1]，则i+1放的苹果需要比i多一个
        - ratings[i] >= ratings[i+1]，则i+1只需要放一个苹果

    向右遍历，若
        - ratings[i] > ratings[i+1]，则i放的苹果需要比i+1多一个
        - ratings[i] <=> ratings[i+1]，则i只需要放一个苹果

    同一个位置需要取大者
    """

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        numbers = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                numbers[i] = numbers[i - 1] + 1

        total = numbers[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                numbers[i] = max(numbers[i], numbers[i + 1] + 1)
            total += numbers[i]
        return total


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().candy(i)}')
