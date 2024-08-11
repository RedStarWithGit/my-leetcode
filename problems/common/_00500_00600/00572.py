#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/subtree-of-another-tree/description/?envType=daily-question&envId=2024-08-04
# ============================================================
"""
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot
具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。
tree 也可以看做它自身的一棵子树。
"""
from typing import Optional, List


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
    对齐根节点，递归即可
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False

        roots = [root]
        for r in roots:
            if self.is_tree_equal(r, subRoot):
                return True
            if r:
                roots.append(r.left)
                roots.append(r.right)
        return False

    def is_tree_equal(self, root0: TreeNode, root1: TreeNode) -> bool:
        if not root0 and not root1:
            return True
        if (not root0 and root1) or (root0 and not root1):
            return False

        return (root0.val == root1.val and self.is_tree_equal(root0.left, root1.left)
                and self.is_tree_equal(root0.right, root1.right))


class Solution2:
    """
    先序遍历，根节点 - 左子树 - 右子树
    若subRoot为某个子树，自然会重合
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inorder(node: TreeNode, results: List[str]):
            if not node:
                results.append('N')
                return

            results.append(str(node.val))
            inorder(node.left, results)
            inorder(node.right, results)

        root_results = []
        inorder(root, root_results)
        sub_results = []
        inorder(subRoot, sub_results)

        return f".{'.'.join(sub_results)}." in f".{'.'.join(root_results)}."


if __name__ == '__main__':
    solution = Solution2
    from helper.tree import create_binary_tree_for_leetcode_input

    for idx, (i, o) in enumerate([
        ((r'root = [3,4,5,1,2,null,null,null,null,0]', r'root = [4,1,2]'), False),
        ((r'root = [3,4,5,1,2]', r'root = [4,1,2]'), True),
        ((r'root = [12]', r'root = [2]'), False),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        r0 = create_binary_tree_for_leetcode_input(i[0], TreeNode)
        r1 = create_binary_tree_for_leetcode_input(i[1], TreeNode)
        print(f'\toutput: {solution().isSubtree(r0, r1)}')
