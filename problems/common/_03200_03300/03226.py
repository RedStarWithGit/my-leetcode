#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/description/?envType=daily-question&envId=2024-11-02
# ============================================================

"""
给你两个正整数 n 和 k。
你可以选择 n 的 二进制表示 中任意一个值为 1 的位，并将其改为 0。
返回使得 n 等于 k 所需要的更改次数。如果无法实现，返回 -1。
"""


class Solution:
    """
    遍历即可
    """

    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0

        n_bits = bin(n)[2:]
        k_bits = bin(k)[2:]
        n_len = len(n_bits)
        k_len = len(k_bits)
        if n_len > k_len:
            k_bits = '0' * (n_len - k_len) + k_bits
        elif n_len < k_len:
            return -1

        result = 0
        for i in range(n_len):
            if n_bits[i] != k_bits[i]:
                if k_bits[i] == '1':
                    return -1
                result += 1
        return result


class Solution2:
    """
    n只能改1为0，不能改0为1。

    n^k：bit位不同的bit置为1
    (n^k) & k: bit位不同且k上对应bit为1的bit置为1
    (n^k) & k != 0：k上有不同位的bit值为1 => return -1
              == 0：取n^k上bit为1的个数
    """

    def minChanges(self, n: int, k: int) -> int:
        tmp = n ^ k
        if tmp & k != 0:
            return -1
        return tmp.bit_count()


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ((13, 4), 2),
        ((21, 21), 0),
        ((14, 13), -1),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().minChanges(*case_input)}')
