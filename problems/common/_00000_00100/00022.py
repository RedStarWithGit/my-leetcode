#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/generate-parentheses/description/
# ============================================================
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

from typing import List


class Solution:
    """
    假定某一状态下：
        已使用的(有left个，已使用的)有right个，此时可用的下一个字符有：
            - (：当left < n
            - )：当left - right > 0
    """

    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        now_str = []
        self.select_next(now_str, 0, 0, n)
        return self.results

    def select_next(self, now_str: List[str], now_left: int, now_right: int, n: int):
        if len(now_str) == n * 2:
            self.results.append(''.join(now_str))
            return

        if now_left < n:
            now_str.append('(')
            self.select_next(now_str, now_left + 1, now_right, n)
            now_str.pop()
        if now_left - now_right > 0:
            now_str.append(')')
            self.select_next(now_str, now_left, now_right + 1, n)
            now_str.pop()


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toputput: {solution().generateParenthesis(i)}')
