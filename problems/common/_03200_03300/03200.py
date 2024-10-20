#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximum-height-of-a-triangle/description/?envType=daily-question&envId=2024-10-01
# ============================================================

"""
给你两个整数 red 和 blue，分别表示红色球和蓝色球的数量。你需要使用这些球来组成一个三角形，
满足第 1 行有 1 个球，第 2 行有 2 个球，第 3 行有 3 个球，依此类推。

每一行的球必须是 相同 颜色，且相邻行的颜色必须 不同。

返回可以实现的三角形的 最大 高度。
"""
import itertools
import math


class Solution:
    """
    相邻行颜色不一致，那么每个颜色的出现次数为：
        - 1开始差为2的等差数列
        - 2开始差为2的等差数列
    """

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def _check(x: int, y: int):
            current_lines = 0
            next_balls = [1, 2]
            remain_balls = [x, y]
            first = True
            while True:
                index = 0 if first else 1
                if remain_balls[index] >= next_balls[index]:
                    remain_balls[index] -= next_balls[index]
                    next_balls[index] += 2
                    current_lines += 1
                    first = not first
                else:
                    break
            return current_lines

        return max(_check(red, blue), _check(blue, red))


class Solution2:
    """
    参考题解：同Solution一样，也是枚举
    """

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        line_balls = [0, 0]
        for i in itertools.count(1):
            line_balls[i % 2] += i
            if not ((red >= line_balls[0] and blue >= line_balls[1]) or (
                    red >= line_balls[1] and blue >= line_balls[0])):
                return i - 1


class Solution3:
    """
    参考题解：直接计算
        - 1开始差为2的等差数列
            若奇数行有k行，则最后一行为2k-1，则总共需要k^2个
        - 2开始差为2的等差数列
            若偶数行有k行，则最后一行为2k，则总共需要(k+1)*k，
            二次函数求大于0的根 k^2 + k - n = 0, k = (-1 + sqrt(1 + 4n)) / 2
        取最小的k所表示的行数+1
    """

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def _compute(x: int, y: int):
            odd_k = int(math.sqrt(x))
            even_k = int((math.sqrt(1 + 4 * y) - 1) / 2)
            return min(2 * odd_k - 1, 2 * even_k) + 1

        return max(_compute(red, blue), _compute(blue, red))


if __name__ == '__main__':
    solution = Solution3

    for idx, (case_input, case_output) in enumerate([
        ((2, 4), 3),
        ((2, 1), 2),
        ((1, 1), 1),
        ((10, 1), 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxHeightOfTriangle(*case_input)}')
