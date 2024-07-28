#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/perfect-squares/description/
# ============================================================
"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，
其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
"""
from helper.func import func_cost_wrapper


class Solution:
    """
    x = x * 1，即x必然存在完全平方数之和的形式
    令f(x)表示题目中x对应的最小值，则
        f(x) = min { f(x-1)+f(1), f(x-4)+f(4), ......, f(x-100)+f(100) }
    """

    squares = [
        i ** 2 for i in range(100, 0, -1)
    ]

    @func_cost_wrapper
    def numSquares(self, n: int) -> int:
        f = [-1] * (n + 1)
        for i in range(1, n + 1):
            if i in self.squares:
                f[i] = 1
            else:
                min_total = i
                for j in self.squares:
                    if i > j:
                        min_total = min(f[j] + f[i - j], min_total)
                f[i] = min_total
        return f[n]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (12, 3),
        (13, 2),
        (7, 4),
        (7168, 4),
        (4128, 3),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().numSquares(i)}')
