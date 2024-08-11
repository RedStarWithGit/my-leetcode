#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
# ============================================================
"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""

from typing import List


class Solution:
    """
    排序然后扫描一遍即可
    常规的基于比较的排序算法是O(nlogn)，可以使用不基于比较的排序算法。
    计数排序会超空间，使用基数排序。
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = self.sort(nums)
        max_value = 1
        current = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                current += 1
                max_value = max(max_value, current)
            elif sorted_nums[i] == sorted_nums[i - 1]:
                pass
            else:
                current = 1
        return max_value

    def sort(self, nums: List[int]):
        positive_nums = []
        negative_nums = []
        for e in nums:
            if e >= 0:
                positive_nums.append(e)
            else:
                negative_nums.append(-e)
        positive_nums = self.radix_sort(positive_nums)
        negative_nums = self.radix_sort(negative_nums)

        results = []
        for i in range(len(negative_nums) - 1, -1, -1):
            results.append(-negative_nums[i])
        for e in positive_nums:
            results.append(e)
        return results

    def radix_sort(self, nums: List[int]):
        divide = 1
        max_value = 10
        while divide:
            slots = [[] for _ in range(10)]
            found_max = False
            for e in nums:
                if e >= max_value:
                    found_max = True
                slots[e // divide % 10].append(e)
            index = 0
            for i in range(10):
                for e in slots[i]:
                    nums[index] = e
                    index += 1
            if found_max:
                divide *= 10
                max_value *= 10
            else:
                divide = None
        return nums


class Solution2:
    """
    官方思路是通过hash来确定是否出现在集合中

    双重循坏，外层全部扫描一遍O(n)，内层当且仅当x-1不在集合中时向上查找最大连续数字
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        max_value = 1
        for x in nums:
            if x - 1 not in nums:
                tmp = x + 1
                while tmp in nums:
                    tmp += 1
                max_value = max(max_value, tmp - x)
        return max_value


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1, 2, 0, 1], 3),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().longestConsecutive(i)}')
