#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
有 n 位玩家在进行比赛，玩家编号依次为 0 到 n - 1 。
给你一个长度为 n 的整数数组 skills 和一个 正 整数 k ，其中 skills[i]
是第 i 位玩家的技能等级。skills 中所有整数 互不相同 。
所有玩家从编号 0 到 n - 1 排成一列。

比赛进行方式如下：
- 队列中最前面两名玩家进行一场比赛，技能等级 更高 的玩家胜出。
- 比赛后，获胜者保持在队列的开头，而失败者排到队列的末尾。

这个比赛的赢家是 第一位连续 赢下 k 场比赛的玩家。
请你返回这个比赛的赢家编号。
"""

from typing import List


class Solution:
    """
    直接模拟下。

    若首位skills为最大值，无需进行额外的比较了。
    """

    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        max_skill = max(skills)
        indexes = [i for i in range(n)]
        current_win_times = 0
        last_win_index = None

        while current_win_times < k:
            x, y = indexes[0], indexes[1]
            if max_skill == skills[x]:
                return x

            if skills[x] > skills[y]:
                indexes.pop(1)
                indexes.append(y)
            else:
                indexes.pop(0)
                indexes.append(x)
            if last_win_index != indexes[0]:
                last_win_index = indexes[0]
                current_win_times = 1
            else:
                current_win_times += 1
        return indexes[0]


class Solution2:
    """
    参考题解：

    大值保留在前面，即要求大值出现后，还需要继续大于接下来的 k - 1个值。
    """

    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        max_value = skills[0]
        max_value_index = 0
        win_times = 0

        for i in range(1, n):
            if max_value > skills[i]:
                win_times += 1
            else:
                max_value_index = i
                max_value = skills[i]
                win_times = 1
            if win_times >= k:
                return max_value_index
        return max_value_index


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([4, 2, 6, 3, 9], 2), 2),
        (([2, 5, 4], 3), 1),
        (([16, 4, 7, 17], 562084119), 3),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().findWinningPlayer(*case_input)}')
