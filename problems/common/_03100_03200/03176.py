#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/description/?envType=daily-question&envId=2024-09-02
# ============================================================
"""
给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在下标范围
[0, seq.length - 2] 中 最多只有 k 个下标 i 满足 seq[i] != seq[i + 1] ，
那么我们称这个整数序列为 好 序列。

请你返回nums中好子序列的最长长度。
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    nums的子序列个数有2**n个，n取值范围[1, 500]，枚举不可行。

    是否可以拆解子问题？
        原问题规模是nums[0:n]，减少规模就是计算nums[0:n-1]
    是否存在状态转移方程？
        令dp[i][j]表示以nums[i]为最后一个元素，且存在j个下标满足seq[x]!=seq[x+1]的子序列的最大长度
        将nums[i]作为子序列的最后一个元素：
            for x in range(i):
                if nums[x] == nums[i]:
                    for j in range(k+1):
                        dp[i][j] = max(dp[x][j] + 1, dp[i][j])
                else:
                    for j in range(k+1):
                        dp[i][j] = max(dp[x][j-1] + 1 if j >= 1 else 1, dp[i][j])
    遍历i即可。O(n * k * n)。
    """

    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = 1
        dp = [[0] * (k + 1) for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            for x in range(i):
                if nums[x] == nums[i]:
                    for j in range(k + 1):
                        dp[i][j] = max(dp[x][j] + 1, dp[i][j])
                else:
                    for j in range(k + 1):
                        dp[i][j] = max(dp[x][j - 1] + 1 if j >= 1 else 1, dp[i][j])
            max_length = max(max_length, max(dp[i]))
        return max_length


class Solution2:
    """
    上面解法临近超时。
    计算dp数组，三重for循环，按题设数据量，操作数大概在10**9左右，可能超时。
    尝试将更新dp[i][j]的操作从O(n)降为O(1)。
    for i in range(1, n):
        for x in range(i):
            if nums[x] == nums[i]:
                for j in range(k + 1):
                    dp[i][j] = max(dp[x][j] + 1, dp[i][j])
            else:
                for j in range(k + 1):
                    dp[i][j] = max(dp[x][j - 1] + 1 if j >= 1 else 1, dp[i][j])
    第一种情况nums[x] == nums[i]：
        在已遍历的nums中与nums[i]相等的数，对应的最大的dp[x][j]。
        假设存在与nums[i]相等的数，且对应的下标为 a < b < c，显然dp[a][j] < dp[b][j] < dp[c][j]。
        因此维护一个dict，key为nums[i]，value为dp[nums[i]]
    第二种请nums[x] != nums[i]：
        在已遍历的nums中与nums[i]不相等的数，对应的最大的dp[x][j-1]。
        维护一个数组max_j，其中max_j[j-1]表示最大的dp[x][j-1]。
    那么：
        for i in range(1, n):
            dp_x = dp[nums[i]]
            for j in range(k + 1):
                dp_x[j] = max(dp_x[j] + 1, max_j[j-1] + 1 if j >= 1 else 1)
            for j in range(k + 1):
                max_j[j] = max(max_j[j], dp_x[j])
    """

    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = 1

        dp = defaultdict(lambda: [0] * (k + 1))
        dp[nums[0]][0] = 1

        max_j = [0] * (k + 1)
        max_j[0] = 1

        for i in range(1, n):
            dp_x = dp[nums[i]]
            for j in range(k + 1):
                dp_x[j] = max(dp_x[j] + 1, max_j[j - 1] + 1 if j >= 1 else 1)
                max_length = max(max_length, dp_x[j])
            for j in range(k + 1):
                max_j[j] = max(max_j[j], dp_x[j])
        return max_length


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([1, 2, 1, 1, 3], 2), 4),
        (([1, 2, 3, 4, 5, 1], 0), 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maximumLength(*case_input)}')
