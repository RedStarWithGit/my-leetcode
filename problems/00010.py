#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/regular-expression-matching/
# ============================================================

"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
"""


class Solution:
    """
    使用动态规划:
    s[0:i]与p[0:j]匹配
        - p[j]不等于*的情况下
            - match_char(s[i], p[j]) and  match_str(s[0:i-1], p[0:j-1])
        - p[j]等于'*'的情况下
            - *取0次：match_str(s[0:i], p[0:j-2])
            - *取1次，match_str(s[0:i], p[0:j-1]) and match_char(s[i], p[j-1])
            - *取1+次：match_str(s[0:i-1], p[0:j]) and match_char(s[i], p[j-1])
    """

    def match_char(self, s, s_index, p, p_index):
        return s[s_index] == p[p_index] or p[p_index] == '.'

    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s) + 1
        p_len = len(p) + 1
        dp = [[False] * p_len for _ in range(s_len)]
        dp[0][0] = True

        s = ' ' + s
        p = ' ' + p
        for i in range(0, s_len):
            for j in range(0, p_len):
                if p[j] != '*':
                    if i >= 1 and j >= 1:
                        dp[i][j] = dp[i - 1][j - 1] and self.match_char(s, i, p, j)
                else:
                    # match_str(s[0:i], p[0:j-2])
                    match = False
                    if not match and j >= 2:
                        match = dp[i][j - 2]
                    # match_str(s[0:i], p[0:j - 1]) and match_char(s[i], p[j - 1])
                    if not match and j >= 1 and i >= 1:
                        match = dp[i][j - 1] and self.match_char(s, i, p, j - 1)
                    # match_str(s[0:i-1], p[0:j]) and match_char(s[i], p[j-1])
                    if not match and i >= 1 and j >= 1:
                        match = dp[i - 1][j] and self.match_char(s, i, p, j - 1)
                    dp[i][j] = match
        return dp[s_len - 1][p_len - 1]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (("aa", "a"), False),
        (("aa", "a*"), True),
        (("ab", ".*"), True),
        (("aab", ".*"), True),
        (("aaa", ".*"), True),
        (("aaa", "ab*a"), False),
        (("aab", "c*a*b"), True),
        (("aaa", "ab*a*c*a"), True),
        (("aaca", "ab*a*c*a"), True),
    ]):
        print(f'case {idx}: {i}')
        print(f'\tpredict: {o}')
        print(f'\toutput: {solution().isMatch(*i)}')
