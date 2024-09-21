#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。
同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位
乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。

给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。

每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x
且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。

返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。

注意：数组 buses 和 passengers 不一定是有序的。
"""
import heapq
import math
from typing import List


class Solution:
    """
    buses和passengers需要升序排序或构造最小堆。
    buses[i]出发，从passengers中取出最大capacity个满足 <= buses[i]的值。
    最后一个去除的passengers[x]，即最后可以上车的乘客到达时间。该乘客：
        - 最后一个bus的最后一个位置：passengers[x] - 1（若存在则继续-1）
        - 最后一个bus的非最后一个位置：last_buses_arrive_time（若存在则继续-1）
    """

    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        heapq.heapify(buses)
        heapq.heapify(passengers)
        last_passenger_arrive_time = math.inf
        last_bus_remain = True
        last_bus_arrive_time = 0
        exists_arrive_time = set()

        while buses:
            last_bus_arrive_time = heapq.heappop(buses)
            remain = capacity
            last_bus_remain = True
            while remain > 0 and passengers and passengers[0] <= last_bus_arrive_time:
                last_passenger_arrive_time = heapq.heappop(passengers)
                exists_arrive_time.add(last_passenger_arrive_time)
                remain -= 1
                last_bus_remain = (remain > 0)
        if last_bus_remain:
            last_passenger_arrive_time = last_bus_arrive_time
        else:
            last_passenger_arrive_time = last_passenger_arrive_time - 1
        while last_passenger_arrive_time in exists_arrive_time:
            last_passenger_arrive_time -= 1
        return last_passenger_arrive_time


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (([5], [7, 8], 1), 5),
        (([2], [2], 2), 1),
        (([10, 20], [2, 17, 18, 19], 2), 16),
        (([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2), 20),
        (([3], [2, 4], 2), 3)
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().latestTimeCatchTheBus(*case_input)}')
