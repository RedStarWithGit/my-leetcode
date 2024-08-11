#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/pascals-triangle/description/
# ============================================================
"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
"""

from typing import List


class Solution:
    """
    简单输出
    """

    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        results = [[1]]
        for i in range(1, numRows):
            lines = [1]
            for j in range(0, i - 1):
                lines.append(results[i - 1][j] + results[i - 1][j + 1])
            lines.append(1)
            results.append(lines)
        return results


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().generate(i)}')
