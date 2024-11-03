#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/?envType=daily-question&envId=2024-11-02
# ============================================================

"""
来自未来的体育科学家给你两个整数数组 energyDrinkA 和 energyDrinkB，数组长度都等于 n。
这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。

你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。然而，如果从一种能量饮料切换到另一种，
你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。

返回在接下来的 n 小时内你能获得的 最大 总强化能量。
注意 你可以选择从饮用任意一种能量饮料开始。
"""

from typing import List


class Solution:
    """
    令dp[i+1][0]表示使用前i个数且最后一次使用A时，能取到的最大值。
    令dp[i+1][1]表示使用前i个数且最后一次使用B时，能取到的最大值。
    显然dp[0][0] = dp[0][1] = 0。

    dp[i+1][0] = max(dp[i][0] + A[i], dp[i-1][1] + A[i])
    dp[i+1][1] = max(dp[i][1] + B[i], dp[i-1][0] + B[i])
    """

    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0, 0] for _ in range(n + 1)]
        for i in range(n):
            if i == 0:
                dp[i + 1][0] = energyDrinkA[i]
                dp[i + 1][1] = energyDrinkB[i]
            else:
                dp[i + 1][0] = max(dp[i][0], dp[i - 1][1]) + energyDrinkA[i]
                dp[i + 1][1] = max(dp[i][1], dp[i - 1][0]) + energyDrinkB[i]
        return max(dp[n][0], dp[n][1])


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([1, 3, 1], [3, 1, 1]), 5),
        (([4, 1, 1], [1, 1, 3]), 7),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxEnergyBoost(*case_input)}')
