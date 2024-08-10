#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/description/?envType=daily-question&envId=2024-08-05
# ============================================================

"""
给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。
"""


class Solution:
    """
    题设n最大取10^9，即0b111011100110101100101000000000，共计30位数。

    先计算下2^n-1（n个1）或者2^n（1后面跟n个0）下有连续1出现的数字的个数：
        - 小于等于n个1的范围符合条件的数字的个数total(n)计算规则为：
            - n位取1的个数first(n)有
                - 11：2^(n-2)
                - 10：total(n-2)
            - n位取0 + n-1位取1：
                - 011：2^(n-3)
                - 010：total(n-3)
            - 类推
            total(n) = first(n) + first(n-1) + ... + first(1) + first(0)

    现计算1xy...yy（x/y合计有n位）下的complex(n+1)个数：
        - 小于等于100...00（1后面跟n个0）的有total(n)个
        - 大于100...00（1后面跟n个0）的有
            - 若x=1，则11开头的有y...yy+1个，10开头的有total(n-1)个
            - 若x=0，有complex(n-1)个
    """

    first = [-1] * 31
    total = [0] * 31

    def compute_by_bits(self):
        self.first[0] = 0
        self.first[1] = 0
        self.total[0] = 0
        self.total[1] = 0
        for i in range(2, 31):
            self.first[i] = 2 ** (i - 2) + self.total[i - 2]
            self.total[i] = self.total[i - 1] + self.first[i]

    def complex(self, number: int, bits: str):
        index = -1
        for i in range(len(bits)):
            if bits[i] == '1':
                index = i
                break

        bits = bits[index:]
        n = len(bits) - 1
        if n < 1:
            return 0

        result = self.total[n]

        if bits[1] == '1':
            number -= 2 ** n + 2 ** (n - 1)
            return result + (number + 1) + self.total[n - 1]

        number -= 2 ** n
        return result + self.complex(number, bits[2:])

    def findIntegers(self, n: int) -> int:
        self.compute_by_bits()
        return n + 1 - self.complex(n, str(bin(n))[2:])


class Solution2:
    """
    官方思路：
    先计算111...111（小于1~后面接x-1个0）时有多少种合理答案，此处官方思路用的是dp。
    dp[0] = 1
    dp[1] = 1
    dp[x] = dp[x-1] + dp[x-2] if x >= 2

    对n，若n & (1~后面跟x-1个0) != 0，说明小于1~(x-1)0的合法数目有dp[x]个
        此时若n & (1~后面跟x-2个0) != 0，说明小于11~(x-2)0且大于等于1~(x-1)0的的合法数目有dp[x-1]个，此时不再继续
        此时若n & (1~后面跟x-2个0) == 0，重新开始计算大于等于1~(x-1)0的合法数目
    """

    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        result = 0
        pre_one = False
        for i in range(29, -1, -1):
            val = 1 << i
            if n & val != 0:
                result += dp[i + 1]
                if pre_one:
                    break
                pre_one = True
            else:
                pre_one = False

            if i == 0:
                # 还有个0
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (16, 9),
        (12, 8),
        (1, 2),
        (2, 3),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 5),
        (7, 5),
        (8, 6),
        (9, 7),
        (10, 8),
        (11, 8),
        (12, 8),
        (0b1111111111, 144),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().findIntegers(i)}')
