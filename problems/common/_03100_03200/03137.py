#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/description/
# ============================================================
"""
给你一个长度为 n 的字符串 word 和一个整数 k ，其中 k 是 n 的因数。

在一次操作中，你可以选择任意两个下标 i 和 j，其中 0 <= i, j < n ，
且这两个下标都可以被 k 整除，然后用从 j 开始的长度为 k 的子串替换从 i
开始的长度为 k 的子串。也就是说，将子串 word[i..i + k - 1] 替换为
子串 word[j..j + k - 1] 。

返回使 word 成为 K 周期字符串 所需的 最少 操作次数。

如果存在某个长度为 k 的字符串 s，使得 word 可以表示为任意次数连接 s ，
则称字符串 word 是 K 周期字符串 。例如，如果 word == "ababab"，
那么 word 就是 s = "ab" 时的 2 周期字符串 。
"""

from collections import Counter
from collections import defaultdict


class Solution:
    """
    取
    word[0:k]
    word[k:2k]
    ......
    word[xk:n]
    中相同字符串最多的来替换别的区间
    """

    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)
        max_value = 0
        for i in range(0, len(word), k):
            d[word[i:k + i]] = d[word[i:k + i]] + 1
            max_value = max(d[word[i:k + i]], max_value)
        return len(word) // k - max_value


class Solution2:
    """
    官方代码
    """

    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        count = Counter(word[i:i + k] for i in range(0, n, k))
        return n // k - max(count.values())


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (("leetcodeleet", 4), 1),
        (("leetcoleet", 2), 3),

    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().minimumOperationsToMakeKPeriodic(*i)}')
