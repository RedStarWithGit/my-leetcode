#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/stamping-the-grid/
# ============================================================

"""
给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
1. 覆盖所有 空 格子。
2. 不覆盖任何 被占据 的格子。
3. 我们可以放入任意数目的邮票。
4. 邮票可以相互有 重叠 部分。
5. 邮票不允许 旋转 。
6. 邮票必须完全在矩阵 内 。
如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
"""

from typing import List


class Solution:
    """
    grid上的每一个空格子必须能够归属于一个stampHeight * stampWidth的矩阵。

    尝试向grid上铺满尽可能多的stampHeight * stampWidth矩阵。
    操作完成后，若存在grid[x][j] == 0的情况则说明有空格子无法占据。
    """

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        if stampWidth == 1 and stampHeight == 1:
            return True

        m = len(grid)
        n = len(grid[0])
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + grid[i][j]

        diffs = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diffs[i][j] = grid[i][j] + (grid[i - 1][j - 1] if i > 0 and j > 0 else 0) - (
                    grid[i][j - 1] if j > 0 else 0) - (grid[i - 1][j] if i > 0 else 0)

        def _get_sum(x0, y0, x1, y1):
            return sums[x1 + 1][y1 + 1] - sums[x1 + 1][y0] - sums[x0][y1 + 1] + sums[x0][y0]

        def _mask_grid(x0, y0, d=2):
            x1 = x0 + stampHeight
            y1 = y0 + stampWidth
            diffs[x0][y0] += d
            if x1 < len(diffs) and y1 < len(diffs[0]):
                diffs[x1][y1] += d
            if y1 < len(diffs[0]):
                diffs[x0][y1] -= d
            if x1 < len(diffs):
                diffs[x1][y0] -= d

        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                if _get_sum(i, j, i + stampHeight - 1, j + stampWidth - 1) == 0:
                    _mask_grid(i, j)

        for i in range(m):
            for j in range(n):
                diffs[i][j] = (diffs[i - 1][j] if i > 0 else 0) + (diffs[i][j - 1] if j > 0 else 0) - (
                    diffs[i - 1][j - 1] if i > 0 and j > 0 else 0) + diffs[i][j]
                if diffs[i][j] == 0:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 4, 3), True),
        (([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 2, 2), False),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().possibleToStamp(*case_input)}')
