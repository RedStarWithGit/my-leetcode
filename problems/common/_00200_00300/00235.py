#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# ============================================================

"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度
尽可能大（一个节点也可以是它自己的祖先）。”
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    给定p、q和root，那么有如下几种情况：
        - p、q中有值与root相等 => 结果是root
        - p、q一个大于root，一个小于root => 结果是root
        - p、q都大于root -> 子问题：给定p、q和root.right
        - p、q都小于root -> 子问题：给定p、q和root.left
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            return root

        if p.val > root.val > q.val:
            return root
        if p.val < root.val < q.val:
            return root

        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)


if __name__ == '__main__':
    solution = Solution
    from helper.tree import create_binary_tree_for_leetcode_input

    for idx, (i, o) in enumerate([
        ((r'root = [6,2,8,0,4,7,9,null,null,3,5]', 2, 8), 6),
        ((r'root = [6,2,8,0,4,7,9,null,null,3,5]', 2, 4), 2),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        root = create_binary_tree_for_leetcode_input(i[0], TreeNode)
        print(f'\toutput: {solution().lowestCommonAncestor(root, TreeNode(i[1]), TreeNode(i[2]))}')
