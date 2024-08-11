#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/second-highest-salary/description/
# ============================================================

"""
Employee 表：
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是这个表的主键。
表的每一行包含员工的工资信息。


查询并返回 Employee 表中第二高的薪水 。如果不存在第二高的薪水，查询应该返回 null(Pandas 则返回 None) 。
"""


class Solution:
    """
    写SQL的

    SELECT
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1
        OFFSET 1
    ) AS SecondHighestSalary
    """
    pass


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([

    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
