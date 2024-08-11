#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/recover-binary-search-tree/description/
# ============================================================

"""
给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
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

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        二叉树中序遍历即一个升序数组，此数组中有两个值位置不对，交换即可。
        正常而言：1,2,3,4,5,6,7,8,9
        有两个值不对(相邻): 2,1,3,4,5,6,7,8,9   -> len(errors) = 1, 交换下标errors[0]和errors[0]+1
        有两个值不对(不相邻): 3,2,1,4,5,6,7,8,9 -> len(errors) = 2, 交换下标errors[0]和errors[1]+1
        """
        errors = []
        nodes = self.to_list(root)
        for i in range(0, len(nodes) - 1):
            if nodes[i].val >= nodes[i + 1].val:
                errors.append(i)
        if len(errors) == 1:
            tmp = nodes[errors[0]].val
            nodes[errors[0]].val = nodes[errors[0] + 1].val
            nodes[errors[0] + 1].val = tmp
        elif len(errors) == 2:
            tmp = nodes[errors[0]].val
            nodes[errors[0]].val = nodes[errors[1] + 1].val
            nodes[errors[1] + 1].val = tmp

    def to_list(self, root: TreeNode) -> List[TreeNode]:
        nodes = []

        def _to_list_impl(root: TreeNode):
            if not root:
                return

            _to_list_impl(root.left)
            nodes.append(root)
            _to_list_impl(root.right)

        _to_list_impl(root)
        return nodes

    def print_tree(self, root: TreeNode):
        return str([e.val for e in self.to_list(root)])


class Solution2:
    """
    官方提供了两种思路，
    一种是中序遍历拿到升序数组后找到问题节点，即上面的实现；
    第二种是第一种的优化，即不需要保存升序数组，在中序遍历期间就找到问题节点；
    """

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.inorder(root)

    def inorder(self, root: TreeNode):
        x = None
        y = None
        count = 0

        nodes = []
        tmp = root
        pre = None

        while tmp or nodes:
            while tmp:
                nodes.append(tmp)
                tmp = tmp.left
            tmp = nodes.pop(-1)
            if pre and tmp.val < pre.val:
                if count == 0:
                    x = pre
                    y = tmp
                    count += 1
                else:
                    y = tmp
                    break

            pre = tmp
            tmp = tmp.right

        x.val, y.val = y.val, x.val


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (r'root = [1, 3, null, null, 2]', '[3, 1, null, null, 2]'),
        (r'root = [1, 2, 3]', '[2, 1, 3]'),
        (r'root = [3, 1, 4, null, null, 2]', '[2, 1, 4, null, null, 3]'),
        (r'root = [6, 9, 3, 1, 5, 7, 11]', '[6, 3, 9, 1, 5, 7, 11]'),
        (r'root = [3,null,2,null,1]', '[1,null,2,null,3]'),
    ]):
        print(f'case {idx}: {i}')
        from helper.tree import create_binary_tree_for_leetcode_input, traverse_binary_tree_for_leetcode_output

        root = create_binary_tree_for_leetcode_input(i, TreeNode)
        solution().recoverTree(root)

        print('\toutput:', traverse_binary_tree_for_leetcode_output(root))
        print('\tpredict:', o)
