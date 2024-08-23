#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/permutation-difference-between-two-strings/description/?envType=daily-question&envId=2024-08-24
# ============================================================

"""
给你两个字符串 s 和 t，每个字符串中的字符都不重复，且 t 是 s 的一个排列。
排列差 定义为 s 和 t 中每个字符在两个字符串中位置的绝对差值之和。
返回 s 和 t 之间的 排列差 。
"""


class Solution:
    """
    只限定小写字母，遍历s获取所有字符对应的index，遍历t求差值即可
    """

    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {}
        for i, ch in enumerate(s):
            d[ch] = i

        result = 0
        for i, ch in enumerate(t):
            result += abs(d[ch] - i)
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (("abc", "bac"), 2),
        (("abcde", "edbac"), 12),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().findPermutationDifference(*i)}')
