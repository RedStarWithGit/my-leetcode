#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/nth-highest-salary/description/
# ============================================================
"""
表: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是该表的主键。
该表的每一行都包含有关员工工资的信息。


查询 Employee 表中第 n 高的工资。如果没有第 n 个最高工资，查询结果应该为 null 。
"""


class Solution:
    """
    CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
    BEGIN
        DECLARE M INT;
        SET M = N - 1;
        RETURN (
            # Write your MySQL query statement below.
            SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1
            OFFSET M
        );
    END
    """
    pass


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([

    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
