#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/clear-digits/description/?envType=daily-question&envId=2024-09-02
# ============================================================
"""
给你一个字符串 s 。
你的任务是重复以下操作删除 所有 数字字符：
删除 第一个数字字符 以及它左边 最近 的 非数字 字符。
请你返回删除所有数字字符以后剩下的字符串。
"""


class Solution:
    """
    遍历，非数字入栈，数字则弹出栈顶元素
    """

    def clearDigits(self, s: str) -> str:
        result = []
        for ch in s:
            if not ch.isdigit():
                result.append(ch)
            elif result:
                result.pop()
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ("abc", "abc"),
        ("cb34", "")
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().clearDigits(case_input)}')
