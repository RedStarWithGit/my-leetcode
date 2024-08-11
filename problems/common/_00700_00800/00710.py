#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/random-pick-with-blacklist/description/
# ============================================================

"""
给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，
从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的
整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可
能性 被返回。

优化你的算法，使它最小化调用语言 内置 随机函数的次数。

实现 Solution 类:
- Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
- int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
"""
import random
from typing import List


class Solution:
    """
    随机返回数组中的一个值，确保返回概率一致：直觉上index来回遍历即可
    1 <= n <= 10^9
    0 <= blacklist[i] < n
    由于数据范围限制，不能直接构造可用数组，否则会超内存，所以必须使用blacklist本身
    双指针
    遇见大blacklist会超时，优化while循环部分
    """

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.blacklist_index = 0
        self.blacklist_size = len(self.blacklist)
        self.n_index = -1
        self.n = n

    def pick(self) -> int:
        self.n_index = (self.n_index + 1) % self.n
        if self.blacklist_size:
            if self.n_index + self.blacklist[self.blacklist_index] + 1 == 0:
                self.blacklist_index = self.blacklist[self.blacklist_index + 1]
                self.n_index = self.blacklist[self.blacklist_index]

            if self.n_index == self.blacklist[self.blacklist_index]:
                start_index = self.blacklist_index
                last_index = start_index
                while self.n_index == self.blacklist[self.blacklist_index]:
                    self.n_index = (self.n_index + 1) % self.n
                    last_index = self.blacklist_index
                    self.blacklist_index = (self.blacklist_index + 1) % self.blacklist_size

                if start_index + 2 < last_index:
                    self.blacklist[start_index] = -self.blacklist[start_index] - 1
                    self.blacklist[start_index + 1] = last_index

            if self.n_index + self.blacklist[self.blacklist_index] + 1 == 0:
                self.blacklist_index = self.blacklist[self.blacklist_index + 1]
                self.n_index = (self.blacklist[self.blacklist_index] + 1) % self.n
                self.blacklist_index = (self.blacklist_index + 1) % self.blacklist_size

        return self.n_index


class Solution2:
    """
    官方思路
    n个数字中有m个数字是黑名单，黑名单要么在区间[0, n-m)，要么在区间[n-m, n)。
    如果黑名单树在区间[0, n-m)，那么映射到区间[n-m, n)中不是黑名单的数字。

    根据条件
        1 <= n <= 109
        0 <= blacklist.length <= min(105, n - 1)
        0 <= blacklist[i] < n
    优先遍历blacklist，而不是遍历n
    """

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        max_seg_blacklist = {i for i in blacklist if i >= n - m}
        to_select_while = n - 1
        self.size = n - m
        self.min_seg_black_2_max_seg_while = {}
        for i in blacklist:
            if i < n - m:
                while to_select_while in max_seg_blacklist:
                    to_select_while -= 1
                self.min_seg_black_2_max_seg_while[i] = to_select_while
                to_select_while -= 1

    def pick(self) -> int:
        x = random.randint(0, self.size - 1)
        return self.min_seg_black_2_max_seg_while.get(x, x)


if __name__ == '__main__':
    solution = Solution2

    a = list(range(1000000))
    a.remove(999)
    for idx, (i, o) in enumerate([
        # ([7, [2, 3, 5]], 7),
        # ([10, [2, 3, 4, 6, 7]], 20),
        ([3, [2]], 20),
        ([20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 16, 17, 19]], 20),
        # ([1000000, a], 99),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        s = solution(*i)
        for i in range(o):
            print(s.pick(), end=', ')
        print('')
