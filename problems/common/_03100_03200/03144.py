#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/description/?envType=daily-question&envId=2024-08-24
# ============================================================

"""
给你一个字符串 s ，你需要将它分割成一个或者更多的 平衡 子字符串。
比方说，s == "ababcc" 那么 ("abab", "c", "c") ，("ab", "abc", "c") 和 ("ababcc") 都是合法分割，
但是 ("a", "bab", "cc") ，("aba", "bc", "c") 和 ("ab", "abcc") 不是，不平衡的子字符串用粗体表示。

请你返回 s 最少 能分割成多少个平衡子字符串。

注意：一个 平衡 字符串指的是字符串中所有字符出现的次数都相同。
"""
from collections import Counter


class Solution:
    """
    令dp[i]为s[0:i]的平衡子字符串分割最小数目，那么
        dp[j] = min{dp[i] + 1}，当且仅当s[i:j]是平衡子字符串，0 <= i < j
    dp[0] = 0

    如何判断一个字符串是不是平衡的？（字符串中所有字符出现的次数相等）
        字符种类 * 最大的出现次数 = 字符串长度

    注意：
        1 <= s.length <= 1000，只能选择O(n^2)的算法。
    """

    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            counter = Counter()
            max_times = 0
            for i in range(j - 1, -1, -1):
                counter[s[i]] += 1
                if counter[s[i]] > max_times:
                    max_times = counter[s[i]]
                if max_times * len(counter) == j - i:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ("fabccddg", 3),
        ("abababaccddb", 2),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().minimumSubstringsInPartition(i)}')
