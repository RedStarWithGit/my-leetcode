#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/bus-routes/description/
# ============================================================

"""
给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，
第 i 辆公交车将会在上面循环行驶。

例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列
1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。
期间仅可乘坐公交车。

求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
"""
import queue
from collections import defaultdict
from typing import List


class Solution:
    """
    从source广度优先搜索，当遇见target时，此时的访问次数即乘车数目。
    若不存在可访问的未访问结点时，遍历结束。
    """

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        visited_nodes = set()
        visited_routes = [False] * len(routes)
        node_2_routes = defaultdict(list)
        for index, route in enumerate(routes):
            for node in route:
                node_2_routes[node].append(index)

        q = queue.Queue()
        q.put((source, 0))
        visited_nodes.add(source)
        while not q.empty():
            node, transfer_times = q.get()
            if node == target:
                return transfer_times

            for i in node_2_routes[node]:
                if not visited_routes[i]:
                    visited_routes[i] = True
                    for next_node in routes[i]:
                        if next_node not in visited_nodes:
                            visited_nodes.add(next_node)
                            q.put((next_node, transfer_times + 1))
        return -1


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([[1, 2, 7], [3, 6, 7]], 1, 6,), 2),
        (([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12), -1),

    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().numBusesToDestination(*case_input)}')
