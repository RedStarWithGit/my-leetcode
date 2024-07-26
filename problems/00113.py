#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/path-sum-ii/description/
# ============================================================

"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
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
    遍历所有从根节点到叶子节点的路径，并求该路径的和是否等于目标值

    路径：
    先序遍历，遍历的节点入栈，若当前节点为叶子节点，栈即路径
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        nodes = []
        self.paths = []
        self.traverse(root, nodes, targetSum)
        return self.paths

    def traverse(self, root: TreeNode, nodes: List[TreeNode], remain: int):
        if not root:
            return

        nodes.append(root)
        if not root.left and not root.right:
            if root.val == remain:
                self.paths.append([e.val for e in nodes])
            nodes.pop(-1)
            return

        self.traverse(root.left, nodes, remain - root.val)
        self.traverse(root.right, nodes, remain - root.val)
        nodes.pop(-1)


if __name__ == '__main__':
    solution = Solution
    from helper.tree import create_binary_tree_for_leetcode_input

    for idx, (i, o) in enumerate([
        ((r'root = [5,4,8,11,null,13,4,7,2,null,null,5,1]', 22), [[5, 4, 11, 2], [5, 8, 4, 5]]),
        ((r'root = [1,2,3]', 5), []),
        ((r'root = [1,2]', 0), []),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        test_root = create_binary_tree_for_leetcode_input(i[0], TreeNode)
        output = solution().pathSum(test_root, i[1])
        print(f'\toutput: {output}')
