#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/unique-binary-search-trees/description/
# ============================================================
"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不
相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
"""


class Solution:
    """
    任取val作为根节点，则1~val构成左子树，val+1~n构成右子树。
    左子树数目 * 右子树数目则为val作为根节点的树的数目。

    超时，增加剪枝操作。显然长度相同的数组构成的树的数目是一样的，缓存。
    """
    cached = {}

    def numTrees(self, n: int) -> int:
        return self.get_total(1, n)

    def get_total(self, left: int, right: int):
        if left >= right:
            return 1

        total = self.cached.get(right - left + 1, 0)
        if total:
            return total

        total = 0
        for root in range(left, right + 1):
            left_number = self.get_total(left, root - 1)
            right_number = self.get_total(root + 1, right)
            total += left_number * right_number
        self.cached[right - left + 1] = total
        return total


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (3, 5),
        (1, 1)
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().numTrees(i)}')
