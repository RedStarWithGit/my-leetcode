#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/time-needed-to-buy-tickets/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
有 n 个人前来排队买票，其中第 0 人站在队伍 最前方 ，第 (n - 1) 人站在队伍 最后方 。

给你一个下标从 0 开始的整数数组 tickets ，数组长度为 n ，其中第 i 人想要购买的票数为 tickets[i] 。

每个人买票都需要用掉 恰好 1 秒 。一个人 一次只能买一张票 ，如果需要购买更多票，他必须走到  队尾 重新
排队（瞬间 发生，不计时间）。如果一个人没有剩下需要买的票，那他将会 离开 队伍。

返回位于位置 k（下标从 0 开始）的人完成买票需要的时间（以秒为单位）。
"""

from typing import List


class Solution:
    """
    题设数据量直接模拟即可
        - 1 <= n <= 100
        - 1 <= tickets[i] <= 100
    """

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        n = len(tickets)
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    counter += 1
                    if i == k and tickets[i] == 0:
                        return counter
        return -1


class Solution2:
    """
    需要将tickets[k]改为0，即减去本身tickets[k]。
    那么整个tickets数组中每个元素
        - 若i <= k，最多减去tickets[k]
        - 若i > k，最多减去tickets[k] - 1
    """

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        for i, value in enumerate(tickets):
            counter += min(tickets[i], tickets[k] if i <= k else tickets[k] - 1)
        return counter


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([2, 3, 2], 2), 6),
        (([5, 1, 1, 1], 0), 8)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().timeRequiredToBuy(*case_input)}')
