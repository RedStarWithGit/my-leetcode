#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
# ============================================================
"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
"""
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
    最长路径可以视为一颗子树，遍历树中每个节点为根节点且经过该根节点的路径的最大值

    max_length_through_root(root) = 经过某子树根节点的路径的长度的最大值
        = root.val +
          max_length_through_root(root.left) +
          max_length_through_root(root.right)
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_length = root.val
        self.max_node = root
        self.nodes = []
        self.max_length_through_root(root)
        return self.max_length

    def max_length_through_root(self, root):
        if not root:
            return 0
        if root.val > self.max_node.val:
            self.max_node = root

        left = self.max_length_through_root(root.left)
        right = self.max_length_through_root(root.right)

        now = max(root.val, root.val + left, root.val + right, root.val + left + right)
        if now > self.max_length:
            self.max_length = now

        if left > 0 and left > right:
            now = root.val + left
        elif right > 0 and right > left:
            now = root.val + right
        else:
            now = root.val

        if now < 0:
            now = 0
        return now


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ('root = [1,2,3]', 6),
        ('root = [-10,9,20,null,null,15,7]', 42),
        ('root = [-1]', -1),
        ('root = [-1, -2, -3]', -1),
        ('root = [5,4,8,11,null,13,4,7,2,null,null,null,1]', 48),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')

        from helper.tree import create_binary_tree_for_leetcode_input

        r = create_binary_tree_for_leetcode_input(i, TreeNode)
        print(f'\toutput: {solution().maxPathSum(r)}')
