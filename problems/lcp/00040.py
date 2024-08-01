#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/uOAnQW/description/?envType=daily-question&envId=2024-08-01
# ============================================================
"""
「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，
若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。
给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选
手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。
"""

from typing import List


class Solution:
    """
    降序排序，取最大的cnt个数字。
    - 若为偶数，则为结果
    - 若为奇数，则需要从已选取的cnt中挑一个奇数转偶数或挑一个偶数转奇数：
        - 用最小的奇数换剩下最大的偶数 or 用最小的偶数换剩下最大的奇数 (取差最小的)

    """

    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards = sorted(cards, reverse=True)

        min_even = None
        min_odd = None
        total = 0

        for i in range(cnt):
            total += cards[i]
            if cards[i] % 2 == 0:
                min_even = cards[i]
            else:
                min_odd = cards[i]

        if total % 2 == 0:
            return total

        min_even_diff = None
        min_odd_diff = None
        for i in range(cnt, len(cards)):
            if min_odd_diff is None and min_odd is not None and cards[i] % 2 == 0:
                min_odd_diff = min_odd - cards[i]
            if min_even_diff is None and min_even is not None and cards[i] % 2 == 1:
                min_even_diff = min_even - cards[i]
            if min_even_diff and min_odd_diff:
                break
        if not min_odd_diff and not min_even_diff:
            return 0
        total -= min(999999 if not min_odd_diff else min_odd_diff, 999999 if not min_even_diff else min_even_diff)
        return total


class Solution2:
    """
    官方给了两个思路：第一个如上，第二个使用计数排序降为O(n)
    """

    def sort(self, nums: List[int]):
        values = [0] * 1001
        for each in nums:
            values[each] += 1
        results = []
        for i in range(len(values) - 1, 0, -1):
            if values[i]:
                results.extend([i] * values[i])
        return results

    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards = self.sort(cards)

        min_even = None
        min_odd = None
        total = 0

        for i in range(cnt):
            total += cards[i]
            if cards[i] % 2 == 0:
                min_even = cards[i]
            else:
                min_odd = cards[i]

        if total % 2 == 0:
            return total

        min_even_diff = None
        min_odd_diff = None
        for i in range(cnt, len(cards)):
            if min_odd_diff is None and min_odd is not None and cards[i] % 2 == 0:
                min_odd_diff = min_odd - cards[i]
            if min_even_diff is None and min_even is not None and cards[i] % 2 == 1:
                min_even_diff = min_even - cards[i]
            if min_even_diff and min_odd_diff:
                break
        if not min_odd_diff and not min_even_diff:
            return 0
        total -= min(999999 if not min_odd_diff else min_odd_diff, 999999 if not min_even_diff else min_even_diff)
        return total


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (([1, 2, 8, 9], 3), 18),
        (([3, 3, 1], 1), 0)
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().maxmiumScore(*i)}')
