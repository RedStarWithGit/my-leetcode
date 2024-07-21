"""
57ms 击败6.26%
减少不必要的操作, 如left或right为None时无需set, 默认情况即可 (22 ~ 23)
46ms 击败54.91%
减少不必要的操作, 0 or -1时会多设置None, 特殊处理
42ms 击败77.13%

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

        if len(values) == 1:
            return [TreeNode(values[0])]

        results = []
        # i == 0 or i == len - 1特殊处理
        for right in self.create_bst(values[1:]):
            root = TreeNode(values[0])
            root.right = right
            results.append(root)

        for left in self.create_bst(values[0:-1]):
            root = TreeNode(values[-1])
            root.left = left
            results.append(root)

        for i in range(1, len(values) - 1):
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
