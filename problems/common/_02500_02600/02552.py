#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/count-increasing-quadruplets/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。

如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的：
- 0 <= i < j < k < l < n 且
- nums[i] < nums[k] < nums[j] < nums[l] 。
"""
from typing import List


class Solution:
    """
    数据范围：4 <= nums.length <= 4000，不能使用O(n^3)以上的算法。

    i < j < k < l 且 nums[i] < nums[k] < nums[j] < nums[l]，
    下标为1234，对应的value需要为1324。
    可以枚举j、k，先满足j、k的条件，然后取j前面小于nums[k]的数目 * k后面大于nums[j]的数目，遍历求和。

    j前面小于nums[k]的数目：
        - 固定nums[k]，遍历j < nums[k]，再遍历 i < j计算小于nums[k]的数目，全部计算O(n^3)。
        - dp，定义less[k][j]，less[k][j+1] = less[k][j] + (1 if nums[j+1] < nums[k] else 0)
    k后面大于nums[j]的数目：
        dp，定义greater[j][k]，greater[j][k-1] = greater[j][k] + (1 if nums[k-1] > nums[j] else 0)
    """

    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)

        less = [[0 for _ in range(n)] for _ in range(n)]
        for k in range(1, n):
            less[k][0] = 1 if nums[0] < nums[k] else 0
            for j in range(k - 1):
                less[k][j + 1] = less[k][j] + (1 if nums[j + 1] < nums[k] else 0)

        greater = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n - 1):
            greater[j][n - 1] = 1 if nums[n - 1] > nums[j] else 0
            for k in range(n - 1, j, -1):
                greater[j][k - 1] = greater[j][k] + (1 if nums[k - 1] > nums[j] else 0)

        result = 0
        for j in range(1, n - 2):
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    result += (less[k][j] * greater[j][k])
        return result


class Solution2:
    """
    官方题解：核心思路仍然是遍历j、k，然后确定满足条件的i的个数和l的个数，相乘求和。

    当j变化成j+1后，i可以取到j，那么满足nums[i] < nums[k]的i的个数可能会发生变化。
        由于nums是1..n的全排列，那么只有对nums[k] > nums[j]的k而言，对应的i的个数会+1。
        count_i = [0] * (n+1)
        for j in range(0, n):
            for x in range(nums[j]+1, n+1):
                count_i[x] += 1

    那如何确定满足nums[j] < nums[l]的l的个数呢？
        固定j后，遍历k，由于l > k，可以让k递减遍历，当nums[k] > nums[j]时+1.

        count_i = [0] * (n+1)
        for j in range(0, n):
            l_count = 0
            for k in range(n-1, j, -1):
                if nums[k] > nums[j]:
                    l_count += 1

            for x in range(nums[j]+1, n+1):
                count_i[x] += 1
    """

    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        count_i = [0] * (n + 1)
        for j in range(0, n):
            l_count = 0
            for k in range(n - 1, j, -1):
                if nums[k] < nums[j]:
                    result += l_count * count_i[nums[k]]
                elif nums[k] > nums[j]:
                    l_count += 1

            for x in range(nums[j] + 1, n + 1):
                count_i[x] += 1
        return result


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([1, 3, 2, 4, 5], 2),
        ([1, 2, 3, 4], 0),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().countQuadruplets(case_input)}')
