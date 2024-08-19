#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/description/
# ============================================================

"""
给你一个整数数组 coins 表示不同面额的硬币，另给你一个整数 k 。

你有无限量的每种面额的硬币。但是，你 不能 组合使用不同面额的硬币。

返回使用这些硬币能制造的 第 kth 小 金额。
"""
import math
from typing import List


class Solution:
    """
    参考题解

    第k-th小的数只会在区间(k, min(coins) * k]。
        - coins中的所有值都大于1，那么k-th最小值必然大于k
        - 若k-th大于min(coins) * k，那么小于k-th的必然至少有k个值，那么这个数不是第k-th小

    给定一个数x，如何判断这个数就是第k-th小呢？
        - 这个数可以被coins组成，即必然是某个coins[i]的倍数，这个不好判断是大了还是小了，不使用
        - 这个数为第k-th小
            - 用coins[0]可以组成 x // coins[0] 个数
            - 用coins[1]可以组成 x // coins[1] 个数
            - ...... 用coins[n-1]可以组成 x // coins[n-1] 个数
            - coins[0]和coins[1]组成相同的数有 x // lcm(coins[0], coins[1]) 个
            - k个coins[i]组成相同的数有 x // lcm(coins[i] for all k) 个，k为奇数时加，k为偶数时减
    """

    def compare(self, coins: List[int], target: int, k: int):
        # coins的子集共有2^n个，不考虑其中的全0组合
        total = 0
        for i in range(1, 2 ** (len(coins))):
            lcm_value = 1
            v = -1
            for j, coin in enumerate(coins):
                if i & (2 ** j) != 0:
                    v = -v
                    lcm_value = math.lcm(lcm_value, coin)
                    if lcm_value > target:
                        break
            else:
                total = total + (target // lcm_value) * v
        if total == k:
            return 0
        return -1 if total < k else 1

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        left = k
        right = min(coins) * k
        value = right

        while left < right:
            mid = (left + right) // 2
            r = self.compare(coins, mid, k)
            if r > 0:
                right = mid
            elif r < 0:
                left = mid + 1
            else:
                value = min(value, mid)
                right = mid
        return value


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (([3, 6, 9], 3), 9),
        (([5, 2], 7), 12),
        (([5], 7), 35),
        (([15, 23, 20, 19, 5, 11, 21, 7, 8, 25], 1394920705), 2758282115)
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().findKthSmallest(*i)}')
