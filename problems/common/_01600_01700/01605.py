#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/description/
# ============================================================

"""
给你两个非负整数数组 rowSum 和 colSum ，其中 rowSum[i] 是二维矩阵中第 i 行元素的和，
colSum[j] 是第 j 列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。

请找到大小为 rowSum.length x colSum.length 的任意 非负整数 矩阵，且该矩阵满足 rowSum 和 colSum 的要求。

请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个 可行矩阵。
"""
from typing import List


class Solution:
    """
    贪心

    matrix[i][j]的取值有如下约束：
    1. >= 0
    2. <= rowSum[i] and <= colSum[j]
    3. sum(rowSum[i][x]) = rowSum[i] and sum(colSum[x][j]) = colSum[j]

    任取一个值令matrix[0][0]满足约束，比如取min(rowSum[0], colSum[0])，
    rowSum[0]和colSum[0]减去使用的数字，此时
        - matrix[0][x]只能取0, x>0
        - 或 matrix[x][0]只能取0, x>0

    继续填补，此流程并不会出现违反上述约束的选择。
    """

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        results = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                min_value = min(rowSum[i], colSum[j])
                results[i][j] = min_value
                rowSum[i] -= min_value
                colSum[j] -= min_value
        return results


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (([3, 8], [4, 7]), [[3, 0], [1, 7]]),
        (([5, 7, 10], [8, 6, 8]), [[0, 5, 0],
                                   [6, 1, 0],
                                   [2, 0, 8]]),

    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutpu: {solution().restoreMatrix(*i)}')
