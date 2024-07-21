#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
# ============================================================

"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n
互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
"""

from my_v2 import Solution

if __name__ == '__main__':
    print(
        Solution().generateTrees(3),
        '\n',
        Solution().generateTrees(1),
        '\n',
        Solution().generateTrees(0),
        '\n',
    )
