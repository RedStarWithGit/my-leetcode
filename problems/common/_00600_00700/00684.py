#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/redundant-connection/?envType=daily-question&envId=2024-10-01
# ============================================================
"""
树可以看成是一个连通且 无环 的 无向 图。

给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，
且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi]
表示图中在 ai 和 bi 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。
如果有多个答案，则返回数组 edges 中最后出现的那个。
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
    给定一个无向连通图，删除一条边（题设保证只需要删除一条）直到成为一个连通无环图（一棵树）。

    最小生成树，遍历edges，若edge的两个端点已经连通，则需要排除。
    使用并查集来表示节点是否连通。
    """

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufs = UnionFindSet(1000)
        for x, y in edges:
            if ufs.is_connected(x, y):
                return [x, y]
            ufs.union(x, y)
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]], [2, 5]),
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().findRedundantConnection(case_input)}')
