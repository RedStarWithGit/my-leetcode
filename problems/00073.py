#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/set-matrix-zeroes/description/
# ============================================================

"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
from typing import List


class Solution:
    """
    记录0的row，col后统一处理
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0


class Solution2:
    """
    要求使用O(1)的空间处理

    使用matrix本身的空间来记录row和col
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zero_in_row0 = any(True for i in range(m) if matrix[0][i] == 0)
        zero_in_col0 = any(True for i in range(n) if matrix[i][0] == 0)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
        if zero_in_row0:
            for j in range(m):
                matrix[0][j] = 0
        if zero_in_col0:
            for i in range(n):
                matrix[i][0] = 0


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        solution().setZeroes(i)
        print(f'\toutput: {i}')
