#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-number-of-robots-within-budget/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，
两者长度都为 n 。第 i 个机器人充电时间为 chargeTimes[i] 单位时间，花费
runningCosts[i] 单位时间运行。再给你一个整数 budget 。

运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，
其中 max(chargeTimes) 是这 k 个机器人中最大充电时间，sum(runningCosts)
是这 k 个机器人的运行时间之和。

请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。
"""
import bisect
from collections import deque
from typing import List


class Solution:
    """
    【连续】运行的机器人数目，这个题目要的是子数组，而非子序列。
    滑动窗口筛选子数组，满足情况时增加right，不满足情况时增加left。

    最重要的是判断[left:right]区间内最大的chargeTimes。
        - right+=1时，取max(max_charge, chargeTimes[right])即可
        - left+=1时
            - 遍历区间[left:right]：O(right-left+1)，最差情况O(n)
            - 对区间[left:right]的chargeTimes升序排序，并记录出现次数，
              left增加时，对应chargeTime的出现次数-1，若为0则移除元素，（该步骤可以使用二分查找）
              max_charge即升序数组的最后一位元素：最差情况O(logn)
    """

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        left = 0
        max_k = 0
        max_charge = 0
        sum_costs = 0
        visited_charges = []

        for right, value in enumerate(chargeTimes):
            if not visited_charges:
                visited_charges.append([value, 1])
            else:
                index = bisect.bisect_right(visited_charges, value, key=lambda x: x[0])
                if index > 0 and visited_charges[index - 1][0] == value:
                    visited_charges[index - 1][1] += 1
                else:
                    visited_charges.insert(index, [value, 1])

            sum_costs += runningCosts[right]
            max_charge = max(max_charge, chargeTimes[right])
            k = right - left + 1

            while k > 0 and max_charge + k * sum_costs > budget:
                sum_costs -= runningCosts[left]
                index = bisect.bisect_right(visited_charges, chargeTimes[left], key=lambda x: x[0])
                visited_charges[index - 1][1] -= 1
                no_max_charges = False
                if visited_charges[index - 1][1] == 0:
                    no_max_charges = visited_charges[index - 1][0] == max_charge
                    visited_charges.pop(index - 1)

                left += 1
                k = right - left + 1
                if k <= 0:
                    max_charge = 0
                    break

                if no_max_charges:
                    max_charge = visited_charges[-1][0]

            if left <= right:
                max_k = max(max_k, right - left + 1)
        return max_k


class Solution2:
    """
    参考题解：使用单调队列来计算[left:right]区间的max_charge。

    遍历right时，队列末尾中所有 <= chargeTimes[right]的元素都需要弹出，然后再补充chargeTimes[right]入队。
    此时队列中维护的元素为：
        [ 比chargeTimes[right-x]大的，比chargeTimes[right]大的，chargeTimes[right] ]
    显然队首元素就是区间[left:right]的max_charge，O(1)。
    """

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        left = 0
        max_k = 0
        sum_costs = 0
        q = deque()

        for right, value in enumerate(chargeTimes):
            while q and value >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)

            sum_costs += runningCosts[right]
            k = right - left + 1

            while k > 0 and chargeTimes[q[0]] + k * sum_costs > budget:
                sum_costs -= runningCosts[left]
                if left == q[0]:
                    q.popleft()
                left += 1
                k = right - left + 1

            max_k = max(max_k, right - left + 1)
        return max_k


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        (([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25), 3),
        (([11, 12, 19], [10, 8, 7], 19), 0),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maximumRobots(*case_input)}')
