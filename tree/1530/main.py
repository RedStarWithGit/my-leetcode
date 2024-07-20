#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/?envType=daily-question&envId=2024-07-18
# ============================================================

import re
import sys

from my_v2 import Solution
from my_v2 import TreeNode

"""
You are given the root of a binary tree and an integer distance.
A pair of two different leaf nodes of a binary tree is said to
be good if the length of the shortest path between them is less
than or equal to distance.

Return the number of good leaf node pairs in the tree.

给定二叉树root和一个distance, 若二叉树的两个叶子节点之间的距离小于等于distance,
则称这两个叶子节点good. 计算该二叉树中所有good的叶子节点集合的数目.
"""


def print_tree(root: TreeNode, depth: int = 0):
    if not root:
        return

    print(f"{'  ' * depth}{root.val}")
    print_tree(root.left, depth + 1)
    print_tree(root.right, depth + 1)


def main(input_string: str):
    """
    :param input_string: 形如root = [1, 2, 3, null, 4], distance = 3
    """
    matcher = re.match(r'root = \[(.+)\], distance = (\d+)', input_string)
    input_node_values = [each.strip() for each in matcher.group(1).split(',')]
    distance = int(matcher.group(2))

    root = TreeNode(int(input_node_values[0]))
    nodes = [root]

    for i in range(1, len(input_node_values)):
        nodes_index = (i - 1) // 2
        left = (i % 2 == 1)
        value = input_node_values[i]
        if value == 'null':
            child_node = None
        else:
            child_node = TreeNode(int(input_node_values[i]))

        if not nodes[nodes_index] and child_node:
            raise Exception("unexpected input")
        if nodes[nodes_index]:
            if left:
                nodes[nodes_index].left = child_node
            else:
                nodes[nodes_index].right = child_node
        nodes.append(child_node)

    # print_tree(root)
    return Solution().countPairs(root, distance)


if __name__ == '__main__':
    for idx, (i, o) in enumerate([
        (r'root = [1,2,3,null,4], distance = 3', 1),
        (r'root = [1,2,3,4,5,6,7], distance = 3', 2),
        (r'root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3', 1),
        (r'root = [15,66,55,97,60,12,56,null,54,null,49,null,9,null,null,null,null,null,90], distance = 5', 3),
    ]):
        print(f'case {idx}: ', end='')
        output_value = main(i)
        print(f'\tpredicate: {o}, real: {output_value}',
              file=sys.stdout if output_value == o else sys.stderr)
