#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/distribute-candies-among-children-ii/description/
# ============================================================

"""
给你两个正整数 n 和 limit 。

请你将 n 颗糖果分给 3 位小朋友，确保没有任何小朋友得到超过 limit 颗糖果，请你返回满足此条件下的 总方案数 。
"""


class Solution:
    """
    显然
        - 若n > limit * 3，则不存在符合题意的结果
        - 若n = limit * 3，仅有(limit, limit, limit)一种方案

    只考虑n < limit * 3的情况，每个人可分配的区间位[0, limit]。
    遍历剪枝
    """

    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            return 0
        if n == limit * 3:
            return 1

        total = 0
        for i in range(min(limit, n), -1, -1):
            remain = n - i
            if remain > limit * 2:
                break

            if remain == limit * 2:
                total += 1
                continue

            # max_value = min(limit, remain)
            # min_value = max(0, remain - limit)
            total += min(limit, remain) - max(0, remain - limit) + 1
        return total


class Solution2:
    """
    显然
        - 若n > limit * 3，则不存在符合题意的结果
        - 若n = limit * 3，仅有(limit, limit, limit)一种方案

    组合。
    由于可以取0，共有C(n+2, 2)种取法。
    其中包括了不合法的取法，即有分隔部分大于limit的情况，
    减去至少一个大于limit的情况，有3 * C(n-limit-1+2, 2)种取法，
    重复减去了至少两个大于limit的情况，需要加上，有3 * C(n - 2*(limit+1) + 2, 2)种取法。
    重复加上了至少三个大于limit的情况，需要减去，有C(n - 3*(limit+1) + 2, 2)种取法。
    """

    def c2(self, n):
        if n < 2:
            return 0
        return n * (n - 1) // 2

    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            return 0
        if n == limit * 3:
            return 1
        return self.c2(n + 2) - 3 * self.c2(n + 1 - limit) + 3 * self.c2(n - 2 * limit) - self.c2(n - 1 - 3 * limit)


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        ((5, 2), 3),
        ((3, 3), 10),
        ((8, 3), 3),
        ((10001, 20005), 50025003),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().distributeCandies(*i)}')
