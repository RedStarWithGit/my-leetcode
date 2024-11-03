#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个仅由数字组成的字符串 s，在最多交换一次 相邻 且具有相同 奇偶性 的数字后，返回可以得到的字典序最小的字符串。

如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。
"""


class Solution:
    """
    最多交换相邻位数一次。
    首先是找到可以交换的两位：相邻位上的数字奇偶性相同
    然后判断是否需要交换：交换后的数要小，即前面位上的数大于后面位上的数

    从高位向低位遍历，满足一次交换或直到遍历完成。
    """

    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1):
            if int(s[i]) % 2 == int(s[i + 1]) % 2 and s[i] > s[i + 1]:
                return s[0:i] + s[i + 1] + s[i] + s[i + 2:]
        return s


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ("45320", "43520"),
        ("001", "001"),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().getSmallestString(case_input)}')
