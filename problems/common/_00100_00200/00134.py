#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/gas-station/description/
# ============================================================
"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站
需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则
返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
"""
from typing import List

from helper.func import func_cost_wrapper


class Solution:
    """
    每个加油站输入gas[i]，输出cost[i]，增长gas[i] - cost[i]。

    """

    @func_cost_wrapper
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        incres = [gas[i] - cost[i] for i in range(len(gas))]
        # print(incres)
        if sum(incres) < 0:
            return -1

        i = 0
        n = len(incres)
        while i < n:
            found = True
            sum_total = 0
            for j in range(i, i + n):
                sum_total += incres[j % n]
                if sum_total < 0:
                    found = False
                    i = j
                    break
            if found:
                return i
            i += 1
        return -1


class Solution2:
    """
    一个有意思的解法：https://leetcode.cn/problems/gas-station/solutions/54278/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/

    首先确定一件事：当sum(gas) >= sum(cost)时，一定能完成环路。
        证明：简化为一个数组increment[i] = gas[i] - cost[i]
             若sum(increment[0:i])<0，那么剩余部分sum(increment[i+1:])必然>0
             此时若increment[i+1:]前面存在部分区间sum(increment[i+1:j])<0，
             那么可以把[i+1:j]部分挪到[0:i]，即又回归到原来的假设。
             总之，必然存在一个increment[i+1:]，其sum足以覆盖后面所有的亏空。

    在确定存在环路的情况下，绘制一个剩余的携带油量曲线图remain，只需要保证这个曲线图永远>=0即可。
    即remain[i]>=0对所有的i恒成立。
    我们任意选择一个点开始绘制remain曲线，其必然有一个最小值（设下标为k），此最小值即亏空最大的地方。
    我们将remain曲线向上平移，使得remain[k] = 0，那么此时整个remain曲线都有remain[i]>=0。
    此时k+1则为我们选择的开始点。
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_total = sum(gas)
        cost_total = sum(cost)
        if gas_total < cost_total:
            return -1

        min_value = 0
        min_index = -1
        remain = 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < min_value:
                min_value = remain
                min_index = i
        return min_index + 1


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
        (([2, 3, 4], [3, 4, 3]), -1),
        (([0 if i != 99999 else 2 for i in range(100000)], [0 if i != 99998 else 1 for i in range(100000)]), 99999),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().canCompleteCircuit(*i)}')
