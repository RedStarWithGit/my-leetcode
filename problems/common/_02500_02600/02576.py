#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个下标从 0 开始的整数数组 nums 。
一开始，所有下标都没有被标记。你可以执行以下操作任意次：

选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。
"""
import bisect
from typing import List


class Solution:
    """
    nums中的数要么作为 2 * nums[i] <= nums[j]中的nums[i]（小的数），要么作为nums[j]（大的数）。
    n = len(nums)，最多有 n // 2 个 (i, j) 对。
    将nums升序排序，显然nums[-1]只能作为大的数参与，且nums[n//2+1]到nums[-1]之间的数都需要作为大的数参与。
    双指针，i从n//2向0移动，j从n-1向n//2+1移动，
        - 若 2 * nums[i] <= nums[j]，标记+2，i-=1，j-=1
        - 若 2 * nums[i] > nums[j]，i-=1
    """

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # first_i = bisect.bisect_right(nums, nums[-1] // 2) - 1
        first_i = (n // 2 - 1) if n % 2 == 0 else (n // 2)
        i = first_i
        j = n - 1
        result = 0
        while i >= 0 and j > first_i:
            if 2 * nums[i] <= nums[j]:
                result += 2
                i -= 1
                j -= 1
            else:
                i -= 1
        return result


class Solution2:
    """
    参考题解，二分法。

    如果能找到k个数对，必然能找到k-1个数对。
    如果不能找到k个数对，必然也不能找到k+1个数对。
    k即答案，取值从0~n//2递增，可以使用二分法。

    如何从nums映射到k？
        若存在k个数对，那么最小的k个数，必然和最大的k个数组成数对。
    """

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def check(k):
            for i in range(k):
                # nums[k-1] vs. nums[n-1]
                # nums[0] vs. nums[n-k]
                if 2 * nums[i] > nums[n - k + i]:
                    return False
            return True

        left = 0
        right = n // 2
        while left < right:
            mid = (left + right) // 2 + 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left * 2


class Solution3:
    """
    参考题解，二分法。使用库函数。

    如果能找到k个数对，必然能找到k-1个数对。
    如果不能找到k个数对，必然也不能找到k+1个数对。
    k即答案，取值从0~n//2递增，可以使用二分法。

    如何从nums映射到k？
        若存在k个数对，那么最小的k个数，必然和最大的k个数组成数对。
    k取值[0,1,...,n//2]，映射为[False,False,False,True,True]，找到第一个True出现的index。
    [0,1,...,n//2][index-1] * 2即为答案。
    """

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def check(k):
            for i in range(k):
                # nums[k-1] vs. nums[n-1]
                # nums[0] vs. nums[n-k]
                if 2 * nums[i] > nums[n - k + i]:
                    return True
            return False

        return (bisect.bisect_left(range(n // 2 + 1), True, key=check) - 1) * 2


if __name__ == '__main__':
    solution = Solution3

    for idx, (case_input, case_output) in enumerate([
        ([3, 5, 2, 4], 2),
        ([9, 2, 5, 4], 4),
        ([7, 6, 8], 0),
        ([20, 30, 60, 15], 4),
        ([42, 83, 48, 10, 24, 55, 9, 100, 10, 17, 17, 99, 51, 32, 16, 98, 99, 31, 28, 68, 71, 14, 64, 29, 15, 40], 26),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxNumOfMarkedIndices(case_input)}')
