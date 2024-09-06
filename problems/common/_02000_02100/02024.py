#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。
老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。

给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。
除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：

每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。
请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。
"""


class Solution:
    """
    允许k次修改字符串，令字符串中连续字符出现的次数最多。

    遍历，当同时出现k个以上的T和F时表示此时不能修改，统计前一个状态下的字符串长度
    """

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_counter = 0
        f_counter = 0
        max_value = 0

        left = 0
        for i, v in enumerate(answerKey):
            if v == 'T':
                t_counter += 1
            else:
                f_counter += 1
            while t_counter > k and f_counter > k:
                if answerKey[left] == 'T':
                    t_counter -= 1
                else:
                    f_counter -= 1
                left += 1
            max_value = max(max_value, i - left + 1)
        return max_value


if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        (("TTFF", 2), 4),
        (("TFFT", 1), 3),
        (("TTFTTFTT", 1), 5),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maxConsecutiveAnswers(*case_input)}')
