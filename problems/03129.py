#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/description/?envType=daily-question&envId=2024-08-06
# ============================================================
"""
给你 3 个正整数 zero ，one 和 limit 。

一个 二进制数组arr 如果满足以下条件，那么我们称它是 稳定的 ：
- 0 在 arr 中出现次数 恰好 为 zero 。
- 1 在 arr 中出现次数 恰好 为 one 。
- arr 中每个长度超过 limit 的 子数组都 同时 包含 0 和 1 。

请你返回 稳定 二进制数组的 总 数目。
由于答案可能很大，将它对 109 + 7 取余 后返回。
"""
import functools


class Solution:
    """
    zero个0，one个1，数组长度zero+one，子数组的长度超过limit时必须包含0和1，即0或者1最多只能连续出现limit次。

    令total(zero, one, limit, 0)表示以0结尾的合法数目，total(zero, one, limit, 1)表示以1结尾的合法数目，有：
        - total(zero, one, limit) = total(zero, one, limit, 0) + total(zero, one, limit, 1)

    在不计算末位0的情况下，total(zero - 1, one, limit)种包含了补上末位0就不合法的1情况，即：
        - 1 + limit个0结尾补上末位0，即去除limit+1个0的情况下以1结尾的合法数目：total(zero - limit - 1, one, limit, 1)
    所以total(zero, one, limit, 0)
        = total(zero - 1, one, limit, 0) + total(zero - 1, one, limit, 1) - total(zero - limit - 1, one, limit, 1)
    同理total(zero, one, limit, 1)
        = total(zero, one - 1, limit, 0) + total(zero, one - 1, limit, 1) - total(zero, one - limit - 1, limit, 0)

    边界条件：
        - zero < 0 or one < 0 => 0
        - zero == 0 and one == 0 => 0
        - zero == 0 => 1 if last != 0 and one <= limit else 0
        - one == 0 => 1 if last != 1 and zero <= limit else 0
    """

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        result = (self.total(zero, one, limit, 0) + self.total(zero, one, limit, 1)) % (10 ** 9 + 7)
        self.total.cache_clear()
        return result

    @functools.cache
    def total(self, zero: int, one: int, limit: int, last: int) -> int:
        if zero < 0 or one < 0:
            return 0
        if zero == 0 and one == 0:
            return 0
        if zero == 0:
            return 1 if last != 0 and one <= limit else 0
        if one == 0:
            return 1 if last != 1 and zero <= limit else 0

        if last == 0:
            # total(zero - 1, one, limit, 0) + total(zero - 1, one, limit, 1) - total(zero - limit - 1, one, limit, 1)
            return (self.total(zero - 1, one, limit, 0)
                    + self.total(zero - 1, one, limit, 1)
                    - self.total(zero - limit - 1, one, limit, 1)) % (10 ** 9 + 7)
        else:
            # total(zero, one - 1, limit, 0) + total(zero, one - 1, limit, 1) - total(zero, one - limit - 1, limit, 0)
            return (self.total(zero, one - 1, limit, 0)
                    + self.total(zero, one - 1, limit, 1)
                    - self.total(zero, one - limit - 1, limit, 0)) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ((1, 1, 2), 2),
        ((1, 2, 1), 1),
        ((3, 3, 2), 14),
        ((19, 15, 15), 855954457),
        ((20, 15, 75), 247943139),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().numberOfStableArrays(*i)}')
