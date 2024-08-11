#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/valid-number/description/
# ============================================================

"""
给定一个字符串 s ，返回 s 是否是一个 有效数字。

例如，下面的都是有效数字："2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
"-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"，而接下来的不是："abc",
"1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"。

一般的，一个 有效数字 可以用以下的规则之一定义：
- 一个 整数 后面跟着一个 可选指数。
- 一个 十进制数 后面跟着一个 可选指数。
    一个 整数 定义为一个 可选符号 '-' 或 '+' 后面跟着 数字。
    一个 十进制数 定义为一个 可选符号 '-' 或 '+' 后面跟着下述规则：
        数字 后跟着一个 小数点 .。
        数字 后跟着一个 小数点 . 再跟着 数位。
        一个 小数点 . 后跟着 数位。
指数 定义为指数符号 'e' 或 'E'，后面跟着一个 整数。
数字 定义为一个或多个数位。
"""
import re


class Solution:
    """
    先用正则试水看看
    """

    def isNumber(self, s: str) -> bool:
        int_pattern = r'[+-]?[0-9]+'
        dec_pattern = r'[+-]?(([0-9]+\.[0-9]*)|(\.[0-9]+))'
        exp_pattern = rf'[eE]{int_pattern}'
        total_pattern = rf'^(({int_pattern})|({dec_pattern}))({exp_pattern})?$'
        return re.match(total_pattern, s) is not None


class Solution2:
    """
    先根据e或E划分前区和后区，后区必须是整数，前区可以是整数或者十进制数
    """

    def isNumber(self, s: str) -> bool:
        before_str = None
        after_str = None
        if 'e' in s or 'E' in s:
            values = s.split('e' if 'e' in s else 'E')
            if len(values) != 2 or not values[1]:
                return False
            before_str = values[0]
            after_str = values[1]
        else:
            before_str = s

        return ((self.is_int(before_str, False) or self.is_dec(before_str))
                and self.is_int(after_str, True))

    def is_dec(self, s: str) -> bool:
        if '.' not in s:
            return False

        values = s.split(r'.')
        if len(values) != 2:
            return False

        before_value = values[0]
        after_value = values[1]

        has_before_number = False
        has_after_number = False

        if before_value:
            index = 0
            if before_value[0] == '+' or before_value[0] == '-':
                index = 1
            for i in range(index, len(before_value)):
                if not 0 <= ord(before_value[i]) - ord('0') <= 9:
                    return False
                has_before_number = True
        if after_value:
            for i in range(len(after_value)):
                if not 0 <= ord(after_value[i]) - ord('0') <= 9:
                    return False
                has_after_number = True
        return has_before_number or has_after_number

    def is_int(self, s: str, result_if_none: bool) -> bool:
        if not s:
            return result_if_none

        has_number = False
        has_sign = False
        if s[0] == '+' or s[0] == '-':
            has_sign = True
        elif 0 <= ord(s[0]) - ord('0') <= 9:
            has_number = True
        else:
            return False

        for i in range(1, len(s)):
            if not 0 <= ord(s[i]) - ord('0') <= 9:
                return False
            has_number = True
        return has_number


class Solution3:
    """
    看了题解，有正则表达式的，有float强转的，官方思路是构造DFA（确定有限状态自动机）。
    用DFA的思路实现一下。
       0    1        2       3        4
     +  -   dot     number  e|E     other
0    1  1   2        8       X        X
1    X  X   2        8       X        X           [+|-]
2    X  X   X        3       X        X           [+|-].
3    X  X   X        4       5        X           [+|-].d
4    X  X   X        4       5        X           [+|-].{d}+
5    6  6   X        7       X        X           [+|-].{d}+[e|E]
6    X  X   X        7       X        X           [+|-].{d}+[e|E][+|-]
7    X  X   X        7       X        X           [+|-].{d}+[e|E][+|-]{d}
8    X  X   9        8       5        X           [+|-]{d}
9    X  X   X        4       5        X           [+|-]{d}.
    """
    states = [
        [1, 2, 8, -1, -1],
        [-1, 2, 8, -1, -1],
        [-1, -1, 3, -1, -1],
        [-1, -1, 4, 5, -1],
        [-1, -1, 4, 5, -1],
        [6, -1, 7, -1, -1],
        [-1, -1, 7, -1, -1],
        [-1, -1, 7, -1, -1],
        [-1, 9, 8, 5, -1],
        [-1, -1, 4, 5, -1]
    ]
    accept_finished_states = {3, 4, 7, 8, 9}

    def get_char_type(self, s: str):
        if s == '+' or s == '-':
            return 0
        if s == '.':
            return 1
        if s == 'e' or s == 'E':
            return 3
        if s.isdigit():
            return 2
        return 4

    def isNumber(self, s: str) -> bool:
        current_state = 0
        for i in range(len(s)):
            current_state = self.states[current_state][self.get_char_type(s[i])]
            if current_state == -1:
                return False
        return current_state in self.accept_finished_states


if __name__ == '__main__':
    solution = Solution3

    for idx, (i, o) in enumerate([
        (r'0', True),
        (r'0123456', True),
        (r'0123456.090', True),
        (r'0e', False),
        (r'e', False),
        (r'.', False),
        (r'-01', True),
        (r'+.', False),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().isNumber(i)}')
