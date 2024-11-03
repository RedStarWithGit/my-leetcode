#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个正整数 n。
如果一个二进制字符串 x 的所有长度为 2 的子字符串中包含 至少 一个 "1"，则称 x 是一个 有效 字符串。

返回所有长度为 n 的 有效 字符串，可以以任意顺序排列。
"""

from typing import List


class Solution:
    """
    内容翻译估计有问题，按题意的不含相邻0的字符串即可。

    从全1的字符串，按间隔+1/+2/...依次调整某位为0。
    """

    def validStrings(self, n: int) -> List[str]:
        results = []
        all_one = ['1'] * n
        results.append(''.join(all_one))

        def _dfs(chars: List[str], current_zero_index: int):
            chars[current_zero_index] = '0'
            results.append(''.join(chars))
            for next_zero_index in range(current_zero_index + 2, n):
                _dfs(chars, next_zero_index)
            chars[current_zero_index] = '1'

        for zero_index in range(n):
            _dfs(all_one, zero_index)
        return results


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (3, ["010", "011", "101", "110", "111"]),
        (1, ["0", "1"]),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().validStrings(case_input)}')
