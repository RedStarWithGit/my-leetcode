#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-points-inside-the-square/description/?envType=daily-question&envId=2024-08-03
# ============================================================

"""
给你一个二维数组 points 和一个字符串 s ，其中 points[i] 表示第 i 个点的坐标，s[i] 表示第 i 个点的 标签 。

如果一个正方形的中心在 (0, 0) ，所有边都平行于坐标轴，且正方形内不存在标签相同的两个点，
那么我们称这个正方形是 合法 的。

请你返回 合法 正方形中可以包含的 最多 点数。

注意：
- 如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。
- 正方形的边长可以为零。
"""
import math
from typing import List
from typing import Set


class Solution:
    """
    一个简单的思路，我们将目标正方形从(0, 0)从边长0向外扩张，若扩张结束，其包含的point数目即结果。
    扩张结束的判定条件？
        此轮扩张导致不满足如下条件：
            - 有point的标签重复
    扩张时使用多长的边？
        每个point(x, y)取最大值max(x, y)后降序排序，每轮扩张使用该边
    """

    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        waitings = []
        for i in range(len(points)):
            waitings.append((max(abs(points[i][0]), abs(points[i][1])), s[i]))
        waitings.sort(key=lambda x: x[0])

        side_length = -1
        point_number = 0
        used_labels = set()

        i = 0
        n = len(waitings)
        while i < n:
            length, label = waitings[i]
            if length != side_length:
                start_index = i
                side_length = length
                while i < n and waitings[i][0] == side_length:
                    i += 1
                number = self.count_okay_points(
                    [value[1] for value in waitings[start_index:i]],
                    used_labels
                )
                if number == 0:
                    break
                point_number += number
        return point_number

    def count_okay_points(self, new_labels: List[str], used_labels: Set[str]):
        origin = len(new_labels)
        new_labels = set(new_labels)
        if origin != len(new_labels):
            return 0

        for label in new_labels:
            if label in used_labels:
                return 0

        used_labels.update(new_labels)
        return len(new_labels)


class Solution2:
    """
    官方思路：

    label只能是小写字母，最多26个label，可以计算每一个label的最小半径。

    最大正方形可用的边长是：
        - 不存在相同label：边长可以无限大
        - 若存在相同label：边长只能是相同label里面较大半径的那个的稍小值
    """

    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        max_length = math.inf
        d = {}

        for i in range(len(s)):
            current_length = max(abs(points[i][0]), abs(points[i][1]))
            if s[i] in d:
                exists_length = d[s[i]]
                if exists_length > current_length:
                    d[s[i]] = current_length
                    max_length = min(max_length, exists_length)
                else:
                    max_length = min(max_length, current_length)
            else:
                d[s[i]] = current_length
        return sum([1 for i in d.values() if i < max_length])


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (([[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], r'abdca'), 2),
        (([[1, 1], [-2, -2], [-2, 2]], r'abb'), 1),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().maxPointsInsideSquare(*i)}')
