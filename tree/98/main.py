#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/validate-binary-search-tree/
# ============================================================
import re
import sys

from my import Solution
from my import TreeNode

"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效二叉搜索树定义如下：
1. 节点的左子树只包含小于当前节点的数。
2. 节点的右子树只包含大于当前节点的数。
3. 所有左子树和右子树自身必须也是二叉搜索树。
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
    matcher = re.match(r'root = \[(.+)\]', input_string)
    input_node_values = [each.strip() for each in matcher.group(1).split(',')]

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
    return Solution().isValidBST(root)


if __name__ == '__main__':
    print(-2 ** 31 - 1, 2 ** 31 - 1 + 1)
    for idx, (i, o) in enumerate([
        (r'root = [2,1,3]', True),
        (r'root = [5,1,4,null,null,3,6]', False),
        (r'root = [2,2,2]', False),
        (r'root = [5,4,6,null,null,3,7]', False),
        (r'root = [34,-6,null,-21]', True),
        (r'root = [2147483647]', True),
    ]):
        print(f'case {idx}: ', end='')
        output_value = main(i)
        print(f'\tpredicate: {o}, real: {output_value}',
              file=sys.stdout if output_value == o else sys.stderr)
