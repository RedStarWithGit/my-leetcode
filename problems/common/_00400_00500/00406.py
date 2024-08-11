#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/queue-reconstruction-by-height/description/
# ============================================================

"""
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。

请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，
其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
"""

from typing import List


class Solution:
    """
    (hi, ki)表示前面存在ki个h大于等于hi
    1. h必然有最大值h_max，该场景下:
        (h_max, 0)：前面没有>=h_max的
        (h_max, 1)：前面有(h_max, 0)
        ……
    针对h_max，可以排序为(h_max, 0), (h_max, 1), ……, (h_max, n)

    2. 不考虑h_max的情况下的h还有最大值h_max_2，该场景有：
        (h_max_2, k)：
            若k=0，只能塞(h_max, 0)前面
            若k!=0，
                k = 1，塞(h_max, 0), (h_max, 1)之间
                k = 2，塞(h_max, 1), (h_max, 2)之间
            即在k下标处insert
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        results = []
        for h, k in people:
            results.insert(k, [h, k])
        return results


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
        ([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]], [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]])
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().reconstructQueue(i)}')
