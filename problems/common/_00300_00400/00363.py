#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/description/?envType=problem-list-v2&envId=prefix-sum
# ============================================================

"""
给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

题目数据保证总会存在一个数值和不超过 k 的矩形区域。
"""
import bisect
import math
from typing import List


class Solution:
    """
    数据范围1 <= m, n <= 100，可以先计算二维前缀和O(m * n)。
    遍历所有的矩阵计算区域和：
        (x0, y0) (x1, y1)唯一确定一个矩阵，
        分别枚举x0、y0、x1、y1，复杂度O(m*n*m*n)，超时。

    遍历所有的矩阵计算区域和：
        - 先确定矩阵的x0、x1，即上下边界 O(m*m)
        - 还需要确定y0、y1以计算出矩阵区域和，此处可以将x0、x1视为一维计算前缀和，那么矩阵区域和为sums[y1+1] - sums[y0]
            即sums[y1+1] - sums[y0] <= k
            遍历sums[y0]并排序，只需要从已排序数据中二分查找即可确定是否满足k
    """

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix_sums[i + 1][j + 1] = prefix_sums[i][j + 1] + prefix_sums[i + 1][j] - prefix_sums[i][j] + \
                                            matrix[i][j]

        def _get_sum(x0: int, y0: int, x1: int, y1: int):
            return prefix_sums[x1 + 1][y1 + 1] - prefix_sums[x1 + 1][y0] - prefix_sums[x0][y1 + 1] + prefix_sums[x0][y0]

        result = -math.inf
        for x0 in range(m):
            for x1 in range(x0, m):
                values = [0]
                for i in range(n):
                    s = _get_sum(x0, 0, x1, i)
                    index = bisect.bisect_left(values, s - k)
                    if index < len(values):
                        result = max(result, s - values[index])
                    bisect.insort_left(values, s)
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 3), 2),
        (([[1, 0, 1], [0, -2, 3]], 2), 2),
        (([[2, 2, -1]], 3), 3),
        (([[2, 2, -1]], 0), -1),

    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxSumSubmatrix(*case_input)}')
