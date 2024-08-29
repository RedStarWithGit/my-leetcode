#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/check-if-grid-satisfies-conditions/description/?envType=daily-question&envId=2024-08-29
# ============================================================

"""
给你一个大小为 m x n 的二维矩阵 grid 。你需要判断每一个格子 grid[i][j] 是否满足：

如果它下面的格子存在，那么它需要等于它下面的格子，也就是 grid[i][j] == grid[i + 1][j] 。
如果它右边的格子存在，那么它需要不等于它右边的格子，也就是 grid[i][j] != grid[i][j + 1] 。
如果 所有 格子都满足以上条件，那么返回 true ，否则返回 false 。
"""

from typing import List


class Solution:
    """
    每列元素必须相同，相邻列元素不能相同3
    """

    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        for col in range(0, n):
            for row in range(1, m):
                if grid[row][col] != grid[row - 1][col]:
                    return False

            if col > 0:
                if grid[0][col] == grid[0][col - 1]:
                    return False

        return True


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([[1, 0, 2], [1, 0, 2]], True),
        ([[1, 1, 1], [0, 0, 0]], False),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().satisfiesConditions(i)}')
