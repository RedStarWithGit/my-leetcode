#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-swap/description/
# ============================================================

"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
"""
import sys


class Solution:
    """
    987654321 -> 987654321
    123456789 -> 923456781  最高位必须是最大的
    123959697 -> 923959617  最高位必须是最大的，最大的有多个选择时，取最小位上的
    """

    def maximumSwap(self, num: int) -> int:
        s = str(num)
        count = {}
        for i in range(0, len(s)):
            count[s[i]] = count.get(s[i], 0) + 1

        max_index = 0
        for i in range(9, -1, -1):
            c = str(i)
            n = count.get(c, 0)

            while n and s[max_index] == c:
                max_index += 1
                if max_index >= len(s):
                    return num
                n -= 1
            if n:
                # change
                for j in range(len(s) - 1, max_index, -1):
                    if s[j] == c:
                        return int(s[0:max_index] + s[j] + s[max_index + 1:j] + s[max_index] + s[j + 1:])
        return num


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (2736, 7236),
        (9973, 9973),
        (1234567890, 9234567810),
        (9876543210, 9876543210),
        (987654321, 987654321),
        (123456789, 923456781),
        (123959697, 923959617),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        r = solution().maximumSwap(i)
        print(f'\toutput: {r}', file=sys.stdout if r == o else sys.stderr)
