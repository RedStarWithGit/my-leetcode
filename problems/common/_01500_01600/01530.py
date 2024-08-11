#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs/description/
# ============================================================

"""
给你二叉树的根节点 root 和一个整数 distance 。
如果二叉树中两个 叶节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。
返回树中 好叶子节点对的数量 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    1. 叶子节点是left和right都为None的节点。
    2. 两个叶子节点必然通过某个子树的根节点相连。
    根据上面两个结论，遍历树的所有子树的根节点，计算该根节点下：
        - 左子树中叶子节点到根节点的路径长
        - 右子树中叶子节点到根节点的路径长
    那么该根节点下好叶子节点对的数目为：
        左子树中路径长 + 右子树路径长 <= distance
    的所有节点对数目。
    """

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        self.get_numbers(root, distance)
        return self.result

    def get_numbers(self, root: TreeNode, distance: int):
        if not root:
            return {}
        if not root.left and not root.right:
            # 到root的路径长: 该长度下的叶子节点数目
            return {0: 1}

        left_numbers = self.get_numbers(root.left, distance)
        left_numbers = {l + 1: n for l, n in left_numbers.items() if l + 1 <= distance}

        right_numbers = self.get_numbers(root.right, distance)
        right_numbers = {l + 1: n for l, n in right_numbers.items() if l + 1 <= distance}
        for l_length, l_no in left_numbers.items():
            for r_length, r_no in right_numbers.items():
                if l_length + r_length <= distance:
                    self.result += l_no * r_no

        for l, n in right_numbers.items():
            if l in left_numbers:
                left_numbers[l] += n
            else:
                left_numbers[l] = n
        return left_numbers


if __name__ == '__main__':
    solution = Solution
    from helper.tree import create_binary_tree_for_leetcode_input

    for idx, (i, o) in enumerate([
        ((r'root = [1,2,3,null,4]', 3), 1),
        ((r'root = [1,2,3,4,5,6,7]', 3), 2),
        ((r'root = [7,1,4,6,null,5,3,null,null,null,null,null,2]', 3), 1),
        ((r'root = [100]', 1), 0),
        ((r'root = [1,1,1]', 2), 1)
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        test_root = create_binary_tree_for_leetcode_input(i[0], TreeNode)
        print(f'\toutput: {solution().countPairs(test_root, i[1])}')
