"""
思路:
1. 两叶子节点必然通过某棵树的根节点互通
2. 某棵树的good leaf node pairs包含3个部分:
2.1. 经过该树根节点的good leaf node pairs
2.2. 左子树的good leaf node pairs
2.3. 右子树的good leaf node pairs
3. 某棵树good leaf node pairs的数目计算
3.1. 计算左子树的good leaf node pairs数目
3.2. 计算右子树的good leaf node pairs数目
3.3. 计算经过根节点的good leaf node pairs数目, 即
     左子树中所有叶子节点到根节点的路径长与
     右子树中所有叶子节点到根节点的路径长的
     和小于distance的节点对数目
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
            return 0, {0: 1}

        left_number, left_leaf_nodes = self._get_leaf_node_number(root.left, distance)
        right_number, right_leaf_nodes = self._get_leaf_node_number(root.right, distance)
        # compute now
        left_leaf_nodes = {k + 1: v for k, v in left_leaf_nodes.items() if k < distance - 1}
        right_leaf_nodes = {k + 1: v for k, v in right_leaf_nodes.items() if k < distance - 1}
        count = left_number + right_number
        if left_leaf_nodes and right_leaf_nodes:
            for d0 in sorted(left_leaf_nodes.keys()):
                for d1 in sorted(right_leaf_nodes.keys()):
                    if d0 + d1 <= distance:
                        count += left_leaf_nodes[d0] * right_leaf_nodes[d1]
                    else:
                        break
        for k, v in right_leaf_nodes.items():
            left_leaf_nodes[k] = left_leaf_nodes.get(k, 0) + v
        return count, left_leaf_nodes
