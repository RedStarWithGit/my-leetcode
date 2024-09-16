#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/points-that-intersect-with-cars/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。
对于任意下标 i，nums[i] = [starti, endi] ，其中 starti 是第 i
辆车的起点，endi 是第 i 辆车的终点。

返回数轴上被车 任意部分 覆盖的整数点的数目。
"""
import bisect
from typing import List


class Solution:
    """
    坐标start,end的数据范围在[1, 100]，使用差分数组，每有汽车覆盖对对应坐标+1。
    """

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        diffs = [0 for _ in range(102)]
        for start, end in nums:
            diffs[start] += 1
            diffs[end + 1] -= 1
        result = 0
        for i in range(1, 101):
            diffs[i] += diffs[i - 1]
            if diffs[i] > 0:
                result += 1
        return result


class Solution2:
    """
    遍历nums，若存在可合并的区间则合并，不存在则添加。

    如何判断是否存在可合并的区间？
        在已访问的区间中存在old_start, old_end，与新访问的区间new_start, new_end满足如下任一关系：
            - new_start <= old_start <= new_end <= old_end : new_start, old_end
            - new_start <= old_start <= old_end <= new_end : new_start, new_end
            - old_start <= new_start <= new_end <= old_end : old_start, old_end
            - old_start <= new_start <= old_end <= new_end : old_start, new_end

    对已访问的区间按start升序排序，然后二分搜索满足new_start <= old_end的区间，若此时
        - new_end < old_start：无需合并
        - new_end >= old_start：需要合并
            合并为min(old_start, new_start), max(old_end, new_end)后继续查看下一个是否需要合并
    """

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = [nums[0]]
        for start, end in nums[1:]:
            insert_index = bisect.bisect_left(points, start, key=lambda x: x[1])

            i = insert_index
            while i < len(points):
                if end < points[i][0]:
                    break

                start = min(points[i][0], start)
                end = max(points[i][1], end)
                i += 1
            while i > insert_index:
                points.pop(insert_index)
                i -= 1
            points.insert(insert_index, (start, end))
        return sum([end - start + 1 for start, end in points])


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([[3, 6], [1, 5], [4, 7]], 7),
        ([[1, 3], [5, 8]], 7),
        ([[2, 3], [3, 9], [5, 7], [4, 10], [9, 10]], 9)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().numberOfPoints(case_input)}')
