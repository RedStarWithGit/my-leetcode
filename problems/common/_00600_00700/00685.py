#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/redundant-connection-ii/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。
该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。

输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。
附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点
ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。

返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
"""

from typing import List


class UnionFindSet(object):

    def __init__(self, n: int):
        self.parents = [i for i in range(n + 1)]

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        self.parents[self.find(x)] = self.find(y)

    def is_connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class Solution:
    """
    在树的基础上加一条边：
    - 若这条边指向树的root节点，则所有节点的入边数为1
        删除这条回路上的任意一条边即可，按题设需要删除最后出现的边，那么如何确定回路上的最后一条边？
        使用并查集，若新的edge的两端节点早已相连，说明该edge是回路上的最后一条边。

    - 若这条边不指向树的root节点：则存在某个节点的入边数为2
        这种情况下的边有两种可能：
            一种是子节点连到非root的祖先节点，构成了一个回路，这种情况必须删除子节点连到祖先节点的edge。
            另一种则是连到子节点或者兄弟节点，删除最后一个边即可。
        需要删除该节点的一条入边，如何确定删除哪条边？
        尝试删除最后一条边，若删除后，该边的两个节点无法相连，说明不能删除这个边，那就删除第一条边。
    """

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        input_nodes = [i for i in range(n + 1)]
        ufs = UnionFindSet(n)

        cycle_edge = None
        node_hava_two_input = None
        two_input_nodes = None

        for x, y in edges:
            if ufs.is_connected(x, y):
                if not cycle_edge:
                    cycle_edge = [x, y]

            if input_nodes[y] != y:
                node_hava_two_input = y
                two_input_nodes = [input_nodes[y], x]
            input_nodes[y] = x
            ufs.union(x, y)

        if node_hava_two_input is None:
            return cycle_edge

        ufs = UnionFindSet(n)
        for x, y in edges:
            if x == two_input_nodes[1] and y == node_hava_two_input:
                continue
            ufs.union(x, y)
        if ufs.is_connected(two_input_nodes[1], node_hava_two_input):
            return [two_input_nodes[1], node_hava_two_input]
        return [two_input_nodes[0], node_hava_two_input]


class Solution2:
    """
    参考题解：
    Solution1主要在两个入边的节点确定如何删除一条入边的逻辑上复杂了。

    假定edge会导致节点存在两个入边，那么此edge的两个节点暂时不加入并查集，这时：
        - 剩下的edge仍能构成回路，说明不该删除这个edge
        - 剩下的edge不能构成回路，说明需要删除这个edge
    """

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        input_nodes = [i for i in range(n + 1)]
        ufs = UnionFindSet(n)

        cycle_edge = None
        node_hava_two_input = None
        two_input_nodes = None

        for x, y in edges:
            if input_nodes[y] != y:
                node_hava_two_input = y
                two_input_nodes = [input_nodes[y], x]
            else:
                if ufs.is_connected(x, y):
                    cycle_edge = [x, y]
                ufs.union(x, y)

            input_nodes[y] = x

        if node_hava_two_input is None:
            return cycle_edge

        if cycle_edge is None:
            return [two_input_nodes[1], node_hava_two_input]
        return [two_input_nodes[0], node_hava_two_input]


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([[2, 1], [3, 1], [4, 2], [1, 4]], [2, 1]),
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().findRedundantDirectedConnection(case_input)}')
