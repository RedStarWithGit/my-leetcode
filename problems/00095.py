#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
# ============================================================
"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且
节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
"""

from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    二叉搜索树是有序的，给定一个数组1~n，任取一个值x为根节点，
    那么左子树只能是由1~x-1构成，右子树只能是x+1~n构成，递归回溯即可。
    """

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nodes = self.create_bst([1, n])
        return nodes

    def create_bst(self, section: List[int]):
        nodes = []
        section_size = section[1] - section[0]
        if section_size < 0:
            return [None]

        if section_size == 0:
            return [TreeNode(section[0])]

        for i in range(section[0], section[1] + 1):
            lefts = self.create_bst([section[0], i - 1])
            rights = self.create_bst([i + 1, section[1]])
            for left in lefts:
                for right in rights:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    nodes.append(root)
        return nodes


if __name__ == '__main__':
    solution = Solution
    from helper.tree import traverse_binary_tree_for_leetcode_output

    for idx, (i, o) in enumerate([
        (3, r'[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]'),
        (1, r'[[1]]')
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        roots = solution().generateTrees(i)
        for root in roots:
            print(traverse_binary_tree_for_leetcode_output(root))
