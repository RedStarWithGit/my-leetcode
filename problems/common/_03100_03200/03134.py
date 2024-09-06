#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/description/?envType=daily-question&envId=2024-08-27
# ============================================================

"""
给你一个整数数组 nums 。数组 nums 的 唯一性数组 是一个按元素从小到大排序的数组，包含了 nums 的所有
非空子数组中不同元素的个数。

换句话说，这是由所有 0 <= i <= j < nums.length 的 distinct(nums[i..j]) 组成的递增数组。
其中，distinct(nums[i..j]) 表示从下标 i 到下标 j 的子数组中不同元素的数量。
返回 nums 唯一性数组 的 中位数 。

注意，数组的 中位数 定义为有序数组的中间元素。如果有两个中间元素，则取值较小的那个。
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    nums数组长度为n，其所有非空子数组：
        - 长度为1的有n个
        - 长度为2的有n-1个
        - ......
        - 长度为n的有1个
    总共有非空子数组n(n+1)//2个。
    每个非空子数组中的不同元素的个数（distinct）为唯一性数组的一个元素，且唯一性数组递增排列。
    题设唯一性数组的中位数，即数组中第 (n(n+1)/2 + 1) // 2 个元素。

    枚举所有非空子数组O(n^2)，题设数据量会超时

    唯一性数组是递增数组，尝试二分，二分范围为[1, n] => O(logn)
    确认distinct <= x的非空子数组个数是否 >= (n(n+1)/2 + 1) // 2，取满足条件的最小x
    """

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        target = ((n + 1) * n // 2 + 1) // 2

        def check(x):
            total = 0
            left = 0

            counter = defaultdict(int)
            for right, value in enumerate(nums):
                counter[value] += 1
                while len(counter) > x:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        counter.pop(nums[left])
                    left += 1
                total += (right - left + 1)
                if total >= target:
                    return True
            return False

        min_value = 1
        max_value = len(set(nums))
        while min_value < max_value:
            medium = (min_value + max_value) // 2
            if check(medium):
                max_value = medium
            else:
                min_value = medium + 1
        return min_value


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([1, 2, 3], 1),
        ([3, 4, 3, 4, 5], 2),
        ([4, 3, 5, 4], 2),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().medianOfUniquenessArray(i)}')
