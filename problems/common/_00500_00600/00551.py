#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/student-attendance-record-i/description/?envType=daily-question&envId=2024-08-18
# ============================================================

"""
给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：

'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in s:
            if i == 'A':
                late = 0
                absent += 1
                if absent >= 2:
                    return False
            elif i == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ("PPALLP", True),
        ("PPALLL", False)
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'	output: {solution().checkRecord(i)}')
