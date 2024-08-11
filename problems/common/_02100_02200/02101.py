#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/detonate-the-maximum-bombs/description/
# ============================================================

"""
给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。

炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。
xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。

你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，
这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。

给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。
"""
from typing import List, Tuple


class Solution:
    """
    有向图
    """

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph, n = self.create_graph(bombs)

        result = 1
        for i in range(n):
            result = max(self.get_longest_path(graph, i), result)
        return result

    def create_graph(self, bombs: List[List[int]]) -> Tuple[List[List[int]], int]:
        n = len(bombs)
        graph = [[0] * n for _ in range(n)]

        for j in range(n):
            for i in range(n):
                if i != j:
                    if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                        graph[i][j] = 1

        return graph, n

    def get_longest_path(self, graph: List[List[int]], start: int) -> int:
        q = [start]
        visited_vertexes = {start}

        for vertex in q:
            for i in range(len(graph)):
                if graph[vertex][i] != 0 and i not in visited_vertexes:
                    visited_vertexes.add(i)
                    q.append(i)
        return len(visited_vertexes)


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([[2, 1, 3], [6, 1, 4]], 2),
        ([[1, 1, 5], [10, 10, 5]], 1),
        ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),
        ([[56, 80, 2], [55, 9, 10], [32, 75, 2], [87, 89, 1], [61, 94, 3], [43, 82, 9], [17, 100, 6], [50, 6, 7],
          [9, 66, 7], [98, 3, 6], [67, 50, 2], [79, 39, 5], [92, 60, 10], [49, 9, 9], [42, 32, 10]], 3),
        ([[6, 47, 162], [993, 41, 133], [185, 745, 196], [229, 88, 226], [476, 578, 437], [988, 729, 262],
          [848, 444, 135], [203, 208, 429], [27, 426, 154], [775, 652, 416], [439, 487, 19], [157, 295, 480],
          [289, 301, 196], [546, 902, 380], [993, 69, 302]], 13),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().maximumDetonation(i)}')
