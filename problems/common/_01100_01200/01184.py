#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/distance-between-bus-stops/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。
我们已知每一对相邻公交站之间的距离，distance[i] 表示
编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。
"""

from typing import List


class Solution:
    """
    要么顺方向，要么反方向，二者取小。
    """

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0

        n = len(distance)
        now = start
        d = 0
        while now != destination:
            d += distance[now]
            now = (now + 1) % n
        now = destination
        d2 = 0
        while now != start:
            d2 += distance[now]
            now = (now + 1) % n
        return min(d, d2)


class Solution2:
    """
    参考题解，使用库函数
    """

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        return min(
            sum(distance[start:destination]),
            sum(distance[0:start]) + sum(distance[destination:])
        )


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([1, 2, 3, 4], 0, 1), 1),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().distanceBetweenBusStops(*case_input)}')
