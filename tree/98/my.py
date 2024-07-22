"""
递归处理
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid_bst(root, -2 ** 31 - 1, 2 ** 31 - 1 + 1)

    def _is_valid_bst(self, root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if not root:
            return True

        if not min_val < root.val < max_val:
            return False

        return (self._is_valid_bst(root.left, min_val, root.val)
                and self._is_valid_bst(root.right, root.val, max_val))
