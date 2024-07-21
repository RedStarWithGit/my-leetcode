"""
root + 左子树bst * 右子树bst, 遍历
"""

from typing import List
from typing import Optional

from node import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.create_bst(list(range(1, n + 1)))

    def create_bst(self, values: List[int]) -> List[Optional[TreeNode]]:
        if not values:
            return [None]

        results = []
        for i in range(0, len(values)):
            root_val = values[i]

            lefts = self.create_bst(values[0:i])
            rights = self.create_bst(values[i + 1:])

            for left in lefts:
                for right in rights:
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    results.append(root)
        return results
