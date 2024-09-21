#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/node-with-highest-edge-score/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个有向图，图中有 n 个节点，节点编号从 0 到 n - 1 ，其中每个节点都 恰有一条 出边。

图由一个下标从 0 开始、长度为 n 的整数数组 edges 表示，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的 有向 边。

节点 i 的 边积分 定义为：所有存在一条指向节点 i 的边的节点的 编号 总和。

返回 边积分 最高的节点。如果多个节点的 边积分 相同，返回编号 最小 的那个。
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    计算入边节点的编号之和。
    """

    def edgeScore(self, edges: List[int]) -> int:
        scores = defaultdict(int)
        for input_node, output_node in enumerate(edges):
            scores[output_node] += input_node

        max_score = 0
        min_node = 0
        for node, score in scores.items():
            if score > max_score:
                max_score = score
                min_node = node
            elif score == max_score:
                min_node = min(node, min_node)
        return min_node


class Solution2:
    """
    计算入边节点的编号之和。一次遍历
    """

    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        max_score = -1
        min_node = -1
        for i, o in enumerate(edges):
            scores[o] += i
            if scores[o] >= max_score:
                min_node = o if scores[o] > max_score else min(o, min_node)
                max_score = scores[o]
        return min_node


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([1, 0, 0, 0, 0, 7, 7, 5], 7),
        ([2, 0, 0, 2], 0),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().edgeScore(case_input)}')
