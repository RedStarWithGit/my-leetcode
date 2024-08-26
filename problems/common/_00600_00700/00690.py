#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/employee-importance/description/?envType=daily-question&envId=2024-08-26
# ============================================================

"""
你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。

给定一个员工数组 employees，其中：
- employees[i].id 是第 i 个员工的 ID。
- employees[i].importance 是第 i 个员工的重要度。
- employees[i].subordinates 是第 i 名员工的直接下属的 ID 列表。
给定一个整数 id 表示一个员工的 ID，返回这个员工和他所有下属的重要度的 总和。
"""

from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    """
    单纯的DFS遍历一棵树
    """

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {e.id: e for e in employees}
        nodes = [mapping[id]]
        result = 0
        for e in nodes:
            result += e.importance
            if e.subordinates:
                nodes.extend([mapping[i] for i in e.subordinates])
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1), 11),
        (([[1, 2, [5]], [5, -3, []]], 5), -3),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        employees = []
        for id, imp, sub in i[0]:
            employees.append(Employee(id, imp, sub))
        print(f'	output: {solution().getImportance(employees, i[1])}')
