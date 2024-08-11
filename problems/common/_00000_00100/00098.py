#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/validate-binary-search-tree/description/
# ============================================================

"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
- 节点的左子树只包含 小于 当前节点的数。
- 节点的右子树只包含 大于 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    按定义递归根节点、左右子树即可
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.is_valid_bst(root, -2 ** 31 - 1, 2 ** 31)

    def is_valid_bst(self, root: Optional[TreeNode], left: int, right: int):
        if not root:
            return True
        if not left < root.val < right:
            return False

        return self.is_valid_bst(root.left, left, root.val) and self.is_valid_bst(root.right, root.val, right)


class Solution2:
    """
    官方给了两种思路：一个是递归左右子树，一个是检查中序遍历是否升序
    现实现中序遍历的思路：中序遍历即按照左子树 - 根节点 - 右子树的顺序遍历
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        root_stack = []
        current_root = root
        min_value = -2 ** 31 - 1

        while root_stack or current_root:
            while current_root:
                root_stack.append(current_root)
                current_root = current_root.left
            current_root = root_stack.pop()

            if current_root.val <= min_value:
                return False

            min_value = current_root.val
            current_root = current_root.right
        return True


if __name__ == '__main__':
    solution = Solution2
    from helper.tree import create_binary_tree_for_leetcode_input

    for idx, (i, o) in enumerate([
        (r'root = [2,1,3]', True),
        (r'root = [2,2,2]', False),
        (r'root = [5,1,4,null,null,3,6]', False),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        test_root = create_binary_tree_for_leetcode_input(i, TreeNode)
        print(f'\toutput: {solution().isValidBST(test_root)}')
