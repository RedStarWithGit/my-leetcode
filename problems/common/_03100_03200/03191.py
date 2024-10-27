#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你一个二进制数组 nums 。

你可以对数组执行以下操作 任意 次（也可以 0 次）：
- 选择数组中 任意连续 3 个元素，并将它们 全部反转 。

反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
请你返回将 nums 中所有元素变为 1 的 最少 操作次数。如果无法全部变成 1 ，返回 -1 。
"""

from typing import List


class Solution:
    """
    模拟，从第一个非1数开始。选择连续三个数执行反转操作。

    设第一个非1数的下标为index：
        - 若index < n - 2，即存在可以反转操作的三个数，执行反转，递增index
        - 若n - 2 <= index < n，无法反转
        - 若index >= n，无需反转
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0
        counter = 0
        while True:
            found = False
            for i in range(index, n):
                if nums[i] == 0:
                    index = i
                    found = True
                    break
            if not found:
                return counter

            if index < n - 2:
                nums[index] = 1
                nums[index + 1] = nums[index + 1] ^ 1
                nums[index + 2] = nums[index + 2] ^ 1
                counter += 1
            elif index < n:
                return -1

        return -1


class Solution2:
    """
    参考题解：
    遍历0~n-2，遇见非0数则执行三个数反转，遍历完成后：
        - 若最后两个数非1，无法达成，返回-1
        - 若最后两个数为1，达成，返回反转操作次数
    """

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0:
                result += 1
                nums[i] = 1
                nums[i + 1] = nums[i + 1] ^ 1
                nums[i + 2] = nums[i + 2] ^ 1
        return result if nums[-1] == 1 and nums[-2] == 1 else -1


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([0, 1, 1, 1, 0, 0], 3),
        ([0, 1, 1, 1], -1),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().minOperations(case_input)}')
