#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-ii/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围
[0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，
那么我们称这个整数序列为 好 序列。

请你返回 nums 中 好 子序列的最长长度
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    和3176一模一样，但是用例数据规模变大了：
        1 <= nums.length <= 5 * 10^3
        0 <= k <= min(50, nums.length)
    如果用O(n * n * k)的算法，估计不能通过，但是3176优化有O(n * k)的算法可以通过。

    解答能通过，但是
    max_length为最大的dp[i][j]，max_j[j]表示最大的dp[x][j]，
    因此无需显示计算max_length，直接获取max(max_j)即可。
    """

    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1

        dp = defaultdict(lambda: [0] * (k + 1))
        dp[nums[0]][0] = 1

        max_j = [0] * (k + 1)
        max_j[0] = 1

        for i in range(1, n):
            dp_x = dp[nums[i]]
            for j in range(k + 1):
                dp_x[j] = max(dp_x[j] + 1, max_j[j - 1] + 1 if j >= 1 else 1)
            for j in range(k + 1):
                max_j[j] = max(max_j[j], dp_x[j])
        return max(max_j)


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([1, 2, 1, 1, 3], 2), 4),
        (([1, 2, 3, 4, 5, 1], 0), 2),
        (([2], 0), 1),
        (([5, 1], 2), 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maximumLength(*case_input)}')
