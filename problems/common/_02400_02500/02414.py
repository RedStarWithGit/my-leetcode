#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz"
的任意子字符串都是 字母序连续字符串 。
- 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。

给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
"""


class Solution:
    """
    遍历，出现连续字符计数+1，非连续字符重置计数
    """
    def longestContinuousSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) != 1:
                max_length = max(max_length, i - start)
                start = i
            else:
                end = i
        return max(max_length, end - start + 1)


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ("abacaba", 2),
        ("abcde", 5),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().longestContinuousSubstring(case_input)}')
