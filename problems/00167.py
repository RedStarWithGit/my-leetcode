#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
# ============================================================

"""
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，
请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是
numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。
"""

from typing import List


class Solution:
    """
    numbers已排序。最开始可以选择[0] + [len - 1]对比target。
    小 + 大 > target: 说明大的大了，需要减少，即len - 1 => len - 2
    小 + 大 < target: 说明小的小了，需要增加，即0 -> 1
    一般化即可。
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            s = numbers[start] + numbers[end]
            if s > target:
                end -= 1
            elif s < target:
                start += 1
            else:
                break
        return [start + 1, end + 1]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (([2, 7, 11, 15], 9), [1, 2]),
        (([2, 3, 4], 6), [1, 3]),
        (([-1, 0], -1), [1, 2]),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().twoSum(*i)}')
