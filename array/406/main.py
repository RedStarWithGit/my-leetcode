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

思路:
1. 相同h时，k小的在前面，k=0的在最前面
2. 相同k时，h小的在前面

按h降序且k升序排列，依次填充数据
"""

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        print(f'sorted: {people}')

        results = []
        for h, k in people:
            results.insert(k, [h, k])
        return results


if __name__ == '__main__':
    for idx, (i, o) in enumerate(
            [
                ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
                ([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]], [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]])
            ]
    ):
        print(f'case {idx}:')
        print(
            Solution().reconstructQueue(i)
        )
        print(o)
        print('\n')
