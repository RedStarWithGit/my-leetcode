#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/make-a-square-with-the-same-color/description/?envType=daily-question&envId=2024-08-27
# ============================================================

"""
给你一个二维 3 x 3 的矩阵 grid ，每个格子都是一个字符，
要么是 'B' ，要么是 'W' 。字符 'W' 表示白色，字符 'B' 表示黑色。

你的任务是改变 至多一个 格子的颜色，使得矩阵中存在一个 2 x 2 颜色完全相同的正方形。

如果可以得到一个相同颜色的 2 x 2 正方形，那么返回 true ，否则返回 false 。
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    任意2*2的格子中有三个或以上的格子字符相等
    """

    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for x, y in [
            (0, 0), (0, 1), (1, 0), (1, 1)
        ]:
            counter = defaultdict(int)
            for x_off, y_off in [
                (0, 0), (0, 1), (1, 0), (1, 1)
            ]:
                counter[grid[x + x_off][y + y_off]] += 1
                if counter[grid[x + x_off][y + y_off]] >= 3:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]], True),
        ([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]], False),
        ([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]], True),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().canMakeSquare(i)}')
