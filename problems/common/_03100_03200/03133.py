#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-array-end/description/?envType=daily-question&envId=2024-08-22
# ============================================================

"""
给你两个整数 n 和 x 。你需要构造一个长度为 n 的 正整数 数组 nums ，
对于所有 0 <= i < n - 1 ，满足 nums[i + 1] 大于 nums[i] ，
并且数组 nums 中所有元素的按位 AND 运算结果为 x 。

返回 nums[n - 1] 可能的 最小 值。
"""


class Solution:
    """
    数组全元素AND结果为x，且数组严格递增

    假定x为100101001，若y & x = x，则必然要求在x出现1的位上，y对应的位必须为1。
    那么y只能在x位为0的位置上切换0/1值。
    y可以切换的数目有2^(0的数目)个，若切换为全1序列后还不够n个数，则往前补1, 10, 11, ......
    """

    def minEnd(self, n: int, x: int) -> int:
        s = bin(x)[2:]
        zero_number = s.count('0')
        if zero_number == 0:
            return int(bin(n - 1)[2:] + s, 2)

        extra_number = (n - 1) // (2 ** zero_number)
        update_zero_number = (n - 1) % (2 ** zero_number)

        s = list(s)
        bits = bin(update_zero_number)[2:]
        bits_index = len(bits) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                s[i] = bits[bits_index]
                bits_index -= 1
                if bits_index == -1:
                    break
        return int(bin(extra_number)[2:] + ''.join(s), 2)


class Solution2:
    """
    官方题解：

    数组单调递增且全&结果为x，显然x为最小值，即nums[0]。
    若存在比x小的值y，那么y至少有一个0的位的位置，对应到x上是1，此时&结果为0，不等于x。

    x的二进制表示下，只看0的位数，将这部分改为n-1，即添加了n-1个数组元素。
    由于没有修改x原来的1位，所以添加的数组元素与x的&结果仍为x。
    """

    def minEnd(self, n: int, x: int) -> int:
        n_bits = bin(n - 1)[2:]
        n_bits_index = len(n_bits) - 1

        x_bits = list(bin(x)[2:])
        for i in range(len(x_bits) - 1, -1, -1):
            if x_bits[i] == '0':
                x_bits[i] = n_bits[n_bits_index]
                n_bits_index -= 1
                if n_bits_index < 0:
                    break
        if n_bits_index >= 0:
            bits = list(n_bits[0:n_bits_index + 1])
            bits.extend(x_bits)
            x_bits = bits
        return int(''.join(x_bits), 2)


class Solution3:
    """
    官方题解代码

    学习下，这里面通过 (x >> i) & 1的值来判断x在第i位（右起0开始计数）是不是0
    """

    def minEnd(self, n: int, x: int) -> int:
        # 结果的二进制表示最多有bitCount位，将x视为全1序列时容易得到该结论
        bitCount = n.bit_length() + x.bit_count()

        res, j = x, 0
        m = n - 1
        for i in range(bitCount):
            # (res >> i) & 1 结果为0表示在x的第i位（右起0开始计数）的值为0，即可能需要发生变化
            if ((res >> i) & 1) == 0:
                # (m >> j) & 1 结果不为0表示在n-1的第j位（右起0开始计数）的值不为0，即需要切换x对应位置的值
                if ((m >> j) & 1) != 0:
                    res |= (1 << i)
                # n-1只能在x的0位置上切换
                j += 1
        return res


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        ((1, 3), 3),
        ((3, 4), 6),
        ((2, 7), 15),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().minEnd(*i)}')
