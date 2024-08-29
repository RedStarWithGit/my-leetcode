#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
# ============================================================
"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的 最少分割次数 。
"""


class Solution:
    """
    令dp[i]表示将s[0:i]分割成所有子字符串都是回文串的最小分割次数。那么
        dp[j] = 0             ，当s[0:j]是回文串
                min{dp[i] + 1}，当s[i:j]是回文串
    字符串长度大于0，i取值 0 < i < j

    令s_dp[i][j]=1表示s[i:j]是为回文串。那么
        当且仅当s[i]==s[j-1]时，s_dp[i][j] = s_dp[i+1][j-1]
        否则s_dp[i][j] = 0
    """

    def minCut(self, s: str) -> int:
        n = len(s)

        s_dp = [[0] * (n + 1) for _ in range(n + 1)]
        for s_len in range(0, n + 1):
            for i in range(0, n - s_len + 1):
                j = i + s_len
                if s_len <= 1:
                    s_dp[i][j] = 1
                else:
                    if s[i] == s[j - 1]:
                        s_dp[i][j] = s_dp[i + 1][j - 1]

        dp = [n + 1] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for j in range(2, n + 1):
            if s_dp[0][j] == 1:
                dp[j] = 0
                continue
            for i in range(j - 1, 0, -1):
                if s_dp[i][j] == 1:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ("aab", 1),
        ("a", 0),
        ("ab", 1),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().minCut(i)}')
