#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/removing-stars-from-a-string/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个包含若干星号 * 的字符串 s 。

在一步操作中，你可以：
- 选中 s 中的一个星号。
- 移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
返回移除 所有 星号之后的字符串。

注意：
- 生成的输入保证总是可以执行题面中描述的操作。
- 可以证明结果字符串是唯一的。
"""


class Solution:
    """
    使用栈存储非*字符，遇*字符弹出栈顶字符，遍历完成后栈中元素即答案
    """

    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().removeStars(case_input)}')
