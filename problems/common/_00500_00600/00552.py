#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/student-attendance-record-ii/description/?envType=daily-question&envId=2024-08-19
# ============================================================

"""
可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。
记录中只含下面三种字符：
'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
- 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
- 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。

给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，
可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 10^9 + 7 取余 的结果。
"""
from typing import List


class Solution:
    """
    dp[n][0|1][0|1|2]表示n次记录下可以获得奖励的次数，
        其中[0|1]表示有几次A，[0|1|2]表示末位是连续几个L
    dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
    dp[i][1][0] = dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2] + dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
    dp[i][0][1] = dp[i-1][0][0]
    dp[i][1][1] = dp[i-1][1][0]
    dp[i][0][2] = dp[i-1][0][1]
    dp[i][1][2] = dp[i-1][1][1]
    """

    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n + 1)]
        dp[1][0][0] = 1
        dp[1][0][1] = 1
        dp[1][1][0] = 1
        for i in range(2, n + 1):
            dp[i][0][0] = dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]
            dp[i][0][0] %= mod

            dp[i][1][0] = dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2] + dp[i - 1][0][0] + dp[i - 1][0][1] + \
                          dp[i - 1][0][2]
            dp[i][1][0] %= mod

            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][0][1] %= mod

            dp[i][1][1] = dp[i - 1][1][0]
            dp[i][1][1] %= mod

            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][0][2] %= mod

            dp[i][1][2] = dp[i - 1][1][1]
            dp[i][1][2] %= mod
        return (sum(dp[n][0]) + sum(dp[n][1])) % mod


class Solution2:
    """
    官方题解：
    由于dp[n]只和dp[n-1]有关，降低空间
    """

    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]
        dp_new = [[0, 0, 0], [0, 0, 0]]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp_new[0][0] = dp[0][0] + dp[0][1] + dp[0][2]
            dp_new[0][0] %= mod

            dp_new[1][0] = dp[1][0] + dp[1][1] + dp[1][2] + dp[0][0] + dp[0][1] + dp[0][2]
            dp_new[1][0] %= mod

            dp_new[0][1] = dp[0][0]
            dp_new[0][1] %= mod

            dp_new[1][1] = dp[1][0]
            dp_new[1][1] %= mod

            dp_new[0][2] = dp[0][1]
            dp_new[0][2] %= mod

            dp_new[1][2] = dp[1][1]
            dp_new[1][2] %= mod

            dp, dp_new = dp_new, dp
        return (sum(dp[0]) + sum(dp[1])) % mod


class Solution3:
    """
    官方题解：
    将dp[n] := dp[n-1]的等式转换为矩阵乘法，n次遍历即矩阵n次幂

    dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
    dp[i][1][0] = dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2] + dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]
    dp[i][0][1] = dp[i-1][0][0]
    dp[i][1][1] = dp[i-1][1][0]
    dp[i][0][2] = dp[i-1][0][1]
    dp[i][1][2] = dp[i-1][1][1]

    改写dp[i]为1*6的矩阵: [ dp[i][0][0], dp[i][1][0], dp[i][0][1], dp[i][1],[1], dp[i][0][2], dp[i][1][2] ]
    dp[i] = dp[i-1] * | 1 1 1 0 0 0 |
                      | 0 1 0 1 0 0 |
                      | 1 1 0 0 1 0 |
                      | 0 1 0 0 0 1 |
                      | 1 1 0 0 0 0 |
                      | 0 1 0 0 0 0 |
    那dp[n] = dp[0] * | 1 1 1 0 0 0 | ^ n
                      | 0 1 0 1 0 0 |
                      | 1 1 0 0 1 0 |
                      | 0 1 0 0 0 1 |
                      | 1 1 0 0 0 0 |
                      | 0 1 0 0 0 0 |
    """

    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7

        matrix = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [1, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0]
        ]

        def matrix_multiply(m0: List[List[int]], m1: List[List[int]]) -> List[List[int]]:
            # m*p x p*m
            m = len(m0)
            p = len(m0[0])
            n = len(m1[0])
            result = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(p):
                        result[i][j] += m0[i][k] * m1[k][j]
                    result[i][j] %= mod
            return result

        dp = [[1, 0, 0, 0, 0, 0]]
        while n > 0:
            if n % 2 == 1:
                dp = matrix_multiply(dp, matrix)
            matrix = matrix_multiply(matrix, matrix)
            n = n // 2
        return sum(dp[0]) % mod


if __name__ == '__main__':
    solution = Solution3

    for idx, (i, o) in enumerate([
        (2, 8),
        (1, 3),
        (10101, 183236316),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().checkRecord(i)}')
