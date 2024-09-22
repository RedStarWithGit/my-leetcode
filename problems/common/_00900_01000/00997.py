#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-town-judge/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：
1. 小镇法官不会信任任何人。
2. 每个人（除了小镇法官）都信任这位小镇法官。
3. 只有一个人同时满足属性 1 和属性 2 。

给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
"""

from typing import List


class Solution:
    """
    存在一个x，不信任任何人，且被n-1个人信任

    题设存在条件：trust 中的所有trust[i] = [ai, bi] 互不相同
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_to_number = [0] * (n + 1)
        trusted_by_number = [0] * (n + 1)
        for a, b in trust:
            trusted_to_number[a] += 1
            trusted_by_number[b] += 1

        result = -1
        for i in range(1, n + 1):
            if trusted_to_number[i] == 0 and trusted_by_number[i] == n - 1:
                if result > 0:
                    return -1
                result = i
        return result


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ((2, [[1, 2]]), 2),
        ((3, [[1, 3], [2, 3]]), 3),
        ((3, [[1, 3], [2, 3], [3, 1]]), -1)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().findJudge(*case_input)}')
