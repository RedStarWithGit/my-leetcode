#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个下标从 0 开始的字符串 text 和另一个下标从 0 开始且长度为 2 的字符串 pattern ，两者都只包含小写英文字母。

你可以在 text 中任意位置插入 一个 字符，这个插入的字符必须是 pattern[0] 或者 pattern[1] 。
注意，这个字符可以插入在 text 开头或者结尾的位置。

请你返回插入一个字符后，text 中最多包含多少个等于 pattern 的 子序列 。
子序列 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。
"""
import math


class Solution:
    """
    pattern仅有两个字符x、y
    若x != y:
        统计text中有多少个x和y，假定其对应的数目为count_x和count_y
            若count_x == count_y：插入x和插入y新增的子序列数目一样
            若count_x > count_y，需要插入y，最多新增count_x个子序列
            若count_x < count_y，需要插入x，最多新增count_y个子序列
        插入之前的子序列数目为：每一个y前面的x数目之和
        该数值加上max(count_x, count_y)即可
    若x == y:
        统计text中有多少个x，假定为count，那么结果为C(count+1, 2)
    """

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        x, y = pattern[0], pattern[1]
        if x == y:
            return math.comb(text.count(x) + 1, 2)

        count_x, count_y = 0, 0
        result = 0
        for v in text:
            if v == y:
                count_y += 1
                result += count_x
            elif v == x:
                count_x += 1
        return result + max(count_x, count_y)


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (("abdcdbc", "ac"), 4),
        (("aabb", "ab"), 6),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maximumSubsequenceCount(*case_input)}')
