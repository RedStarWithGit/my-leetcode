#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
# ============================================================
"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组
[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。
"""

from typing import List

from helper.func import func_cost_wrapper


class Solution:
    """
    计算全部的total[i][j]。
        total[i][j-1] = nums[i]+nums[i+1]+......+nums[j-1]
        total[i][j]   = nums[i]+nums[i+1]+......+nums[j-1]+nums[j]
    全部计算需要O(n^2)。
    遍历这里面大于target且j-i最小的即可。
    超内存了。没必要存储total[i][j]，只需要保留上一个total[i][j-1]即可。
    超时间了。n最大10^5，O(n^2)超时也正常。

    换一个思路，如果存在目标数组，那么必然会在[0:i]达成。
    此时加上[i+1]必然也大于target，那么就需要移动左侧的开始下标，即移动0到1来调整总数。

    """

    @func_cost_wrapper
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        total = 0
        n = len(nums)
        min_length = n + 1
        for i in range(n):
            total += nums[i]
            if total >= target:
                # try to remove start nums
                while total >= target:
                    total -= nums[start]
                    start += 1

                min_length = min(min_length, i - start + 2)
                if min_length == 1:
                    return min_length
        if min_length > n:
            return 0
        return min_length


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ((7, [2, 3, 1, 2, 4, 3]), 2),
        ((4, [1, 4, 4]), 1),
        ((11, [1, 1, 1, 1, 1, 1, 1, 1]), 0),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().minSubArrayLen(*i)}')
