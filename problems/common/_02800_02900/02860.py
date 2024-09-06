#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/happy-students/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，其中 n 是班级中学生的总数。
班主任希望能够在让所有学生保持开心的情况下选出一组学生：

如果能够满足下述两个条件之一，则认为第 i 位学生将会保持开心：
- 这位学生被选中，并且被选中的学生人数 严格大于 nums[i] 。
- 这位学生没有被选中，并且被选中的学生人数 严格小于 nums[i] 。

返回能够满足让所有学生保持开心的分组方法的数目。
"""

from typing import List


class Solution:
    """
    将nums拆分为两个子数组（允许空数组）：
        1）selected：selected数组长度 必须严格大于 selected数组中的所有元素（若selected非空）
        2）not_selected: selected数组长度 必须严格小于 not_selected数组中的所有元素（若non_selected非空）

    往selected数组中添加元素时，必须从添加nums数组中的最小值。
        若未添加最小值，假定添加了nums[j]进入selected，此时仍有nums[i] < nums[j]未添加进selected，此时：
            - 按1）有len(selected) > nums[j] > nums[i]
            - 按2）有len(selected) < nums[i]
        显然不成立，因此selected中只能依次添加nums剩余的最小值

    往selected数组添加元素后，如何判断此时selected有效？
        - selected中的最大值为最后添加的元素selected[-1]，需要满足 len(selected) > selected[-1]
        - non_selected中的最小值为nums剩余的最小值，需要满足 len(selected) < nums[current_index]
    """

    def countWays(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        selected_len = 0

        if nums[0] > 0:
            result += 1

        n = len(nums)
        for i, v in enumerate(nums):
            selected_len += 1
            if selected_len > v and (i == n - 1 or nums[i + 1] > selected_len):
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([1, 1], 2),
        ([6, 0, 3, 3, 6, 7, 2, 7], 3),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().countWays(case_input)}')
