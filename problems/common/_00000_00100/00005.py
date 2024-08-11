#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/longest-palindromic-substring/description/
# ============================================================

"""
给你一个字符串 s，找到 s 中最长的 回文子串。
"""


class Solution:
    """
    回文串对称，可以从中心向两边扩展查找，找到的回文串字符串最长即可
    """

    def longestPalindrome(self, s: str):
        start, end = 0, 0

        for i in range(0, len(s) - 1):
            l, r = self.expand(s, i, i)
            if r - l > end - start:
                start, end = l, r
            l, r = self.expand(s, i, i + 1)
            if r - l > end - start:
                start, end = l, r

        return s[start:end + 1]

    def expand(self, s: str, i: int, j: int):
        n = len(s)

        start, end = i, j
        for k in range(0, n):
            start = i - k
            end = j + k
            if not 0 <= start < n or not 0 <= end < n or start > end:
                break
            if s[start] != s[end]:
                break
        return start + 1, end - 1


class Solution2:
    """
    1. s[i:j]是回文串 = s[i+1:j-1]是回文串且s[i]==s[j]
    2. s[i:i]必然是长度为1的回文串

    从长度1~n遍历，填补dp数组
    """

    def longestPalindrome(self, s: str):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        l, r = 0, 0
        for s_size in range(1, n):
            for start in range(0, n - 1):
                end = start + s_size
                if end >= n:
                    break

                if s[end] == s[start]:
                    if end - 1 <= start + 1:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start + 1][end - 1]

                    if dp[start][end]:
                        if end - start > r - l:
                            l, r = start, end
        return s[l:r + 1]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('bb', 'bb')
    ]):
        print(f'case {idx}: {i}')
        a = solution().longestPalindrome(i)
        print(f'\toutput: {a}')
        print(f'\tpredict: {o}')
