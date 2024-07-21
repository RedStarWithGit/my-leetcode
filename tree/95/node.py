# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        nodes = [str(self.val)]
        nodes.extend(self.nodes())
        return str(nodes)

    def __repr__(self):
        return self.__str__()

    def nodes(self):
        if not self.left and not self.right:
            return []
        nodes = [str(self.left.val) if self.left else 'null', str(self.right.val) if self.right else 'null']
        if self.left:
            nodes.extend(self.left.nodes())
        if self.right:
            nodes.extend(self.right.nodes())
        return nodes
