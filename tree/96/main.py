#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/unique-binary-search-trees/
# ============================================================

"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的
二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
"""

from my import Solution

if __name__ == '__main__':
    print(
        (Solution().numTrees(3), 5),
        '\n',
        (Solution().numTrees(1), 1),
        '\n',
    )

    s = Solution()
    s.numTrees(19)
    print(s.predefined)