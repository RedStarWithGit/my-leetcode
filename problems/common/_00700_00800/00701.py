#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/
# ============================================================
"""
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。
返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。
你可以返回 任意有效的结果 。
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
    BST的insert操作

    就简单的insert就行，没有求平衡之类的约束
    """

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root


if __name__ == '__main__':
    solution = Solution
    from helper.tree import create_binary_tree_for_leetcode_input
    from helper.tree import traverse_binary_tree_for_leetcode_output

    for idx, (i, o) in enumerate([
        ((r'root = [4,2,7,1,3]', 5), '[4,2,7,1,3,5]'),
        ((r'root = [40,20,60,10,30,50,70]', 25), '[40,20,60,10,30,50,70,null,null,25]'),
        ((r'root = [4,2,7,1,3,null,null,null,null,null,null]', 5), '[4,2,7,1,3,5]')
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        test_root = create_binary_tree_for_leetcode_input(i[0], TreeNode)
        test_root = solution().insertIntoBST(test_root, i[1])
        print(f'\toutput: {traverse_binary_tree_for_leetcode_output(test_root)}')
