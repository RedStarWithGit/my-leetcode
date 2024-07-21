"""
[1:n]取i作为root, 则左子树由[1:i-1]构成, 右字数由[i+1:n]构成,
则以i为root的bst的数目为左子树的数目 * 右子树的数目。
在对i=1..n求和即可。
"""


class Solution:
    predefined = {
        0: 1,
        1: 1,
        2: 2,
        3: 5
    }

    def numTrees(self, n: int) -> int:
        return self.get_number(n)

    def get_number(self, n: int) -> int:
        if n in self.predefined.keys():
            return self.predefined[n]

        results = 0
        for i in range(0, n):
            results += self.get_number(i) * self.get_number(n - 1 - i)
        self.predefined[n] = results
        return results
