#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/description/?envType=daily-question&envId=2024-09-01
# ============================================================

"""
给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。
已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。

请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime
处于区间 [startTime[i], endTime[i]]（含）的学生人数。
"""

from typing import List


class Solution:
    """
    简单的大小比较后是否+1
    """

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                result += 1
        return result


class Solution2:
    """
    差分数组
    """

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        diffs = [0] * 1001
        for start, end in zip(startTime, endTime):
            diffs[start] += 1
            diffs[end + 1] -= 1
        return sum(diffs[0:queryTime + 1])


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([1, 2, 3], [3, 2, 7], 4), 1),
        (([4], [4], 4), 1),
        (([4], [4], 5), 0),
        (([1, 1, 1, 1], [1, 3, 2, 4], 7), 0),
        (([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5), 5),
        ((
         [603, 177, 76, 617, 10, 590, 849, 268, 472, 74, 565, 325, 910, 297, 959, 311, 962, 970, 648, 358, 438, 86, 833,
          582, 756, 509, 8, 233, 430, 459, 204, 677, 635, 299, 681, 435, 197, 390, 331, 628, 899, 211],
         [961, 538, 389, 667, 24, 947, 1000, 861, 552, 114, 657, 526, 964, 896, 973, 366, 991, 992, 940, 563, 466, 816,
          988, 722, 852, 542, 523, 934, 777, 772, 487, 700, 698, 785, 741, 791, 310, 775, 917, 774, 978, 920], 383), 0)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().busyStudent(*case_input)}')
