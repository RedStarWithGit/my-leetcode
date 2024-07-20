"""
my.py: 94ms Beats 66.78%
减少sorted次数
my_v2.py: 75ms Beats 91.36%
"""
from typing import Dict
from typing import Tuple


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self._get_leaf_node_number(root, distance)[0]

    def _get_leaf_node_number(self, root: TreeNode, distance: int) -> Tuple[int, Dict[int, int]]:
        if not root:
            return 0, {}

        if not root.left and not root.right:
            return 0, {1: 1}

        left_number, left_leaf_nodes = self._get_leaf_node_number(root.left, distance)
        right_number, right_leaf_nodes = self._get_leaf_node_number(root.right, distance)
        # compute now
        count = left_number + right_number
        if left_leaf_nodes and right_leaf_nodes:
            for d0 in left_leaf_nodes.keys():
                if d0 >= distance:
                    break

                for d1 in right_leaf_nodes.keys():
                    if d0 + d1 <= distance:
                        count += left_leaf_nodes[d0] * right_leaf_nodes[d1]
                    else:
                        break
        for k, v in right_leaf_nodes.items():
            left_leaf_nodes[k] = left_leaf_nodes.get(k, 0) + v
        return count, {k + 1: left_leaf_nodes.get(k) for k in sorted(left_leaf_nodes.keys()) if k < distance - 1}
