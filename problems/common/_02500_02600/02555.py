#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/maximize-win-from-two-segments/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
在 X轴 上有一些奖品。给你一个整数数组 prizePositions ，它按照 非递减 顺序排列，
其中 prizePositions[i] 是第 i 件奖品的位置。数轴上一个位置可能会有多件奖品。
再给你一个整数 k 。

你可以选择两个端点为整数的线段。每个线段的长度都必须是 k 。你可以获得位置在任一线段上
的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。

比方说 k = 2 ，你可以选择线段 [1, 3] 和 [2, 4] ，你可以获得满足
1 <= prizePositions[i] <= 3 或者 2 <= prizePositions[i] <= 4 的所有奖品 i 。
请你返回在选择两个最优线段的前提下，可以获得的 最多 奖品数目。
"""
import bisect
from typing import List


class Solution:
    """
    选取两个区间[x, x+k]和[y, y+k]，令数组满足如下任一条件的i最多
        - x <= prizePositions[i] <= x+k
        - y <= prizePositions[i] <= y+k
    显然[x, x+k]与[y, y+k]不存在重叠部分比存在重叠部分更优。

    枚举区间[y, y+k]，然后从[0, y-1]中挑出最大的[x, x+k]区间，二者求和取最大值。
    令dp[i] = (x_index, prize_total)，表示以prizePositions[i]作为区间最大值的情况下
        - x_index表示区间的最小值对应prizePositions的下标
        - prize_total表示区间可以取得的最大奖品数目
    则dp[i+1]
        - prizePositions[i+1] - prizePositions[x_index] > k，则必须更新x_index
            x_index += 1 直到 prizePositions[new_x_index] != prizePositions[old_x_index]
            dp[i+1].x_index = new_x_index
            dp[i+1].prize_total = dp[i].prize_total + 1 - (new_x_index - old_x_index)
        - prizePositions[i+1] - prizePositions[x_index] <= k，则无需更新x_index
            dp[i+1].x_index = dp[i].x_index
            dp[i+1].prize_total = dp[i].prize_total + 1

    dp[i][1]即以prizePositions[i]结尾时的最大奖品数目，现在还需要以前i个的最大奖品数。
        pre_dp[i] = max(pre_dp[i-1], dp[i][1])
    """

    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [0, 1]
        for i in range(1, n):
            x_index, prize_total = dp[i - 1]
            if prizePositions[i] - prizePositions[x_index] > k:
                new_x_index = x_index
                while prizePositions[i] - prizePositions[new_x_index] > k:
                    new_x_index += 1
                dp[i] = [new_x_index, prize_total + 1 - (new_x_index - x_index)]
            else:
                dp[i] = [x_index, prize_total + 1]

        pre_dp = [0 for _ in range(n)]
        pre_dp[0] = dp[0][1]
        for i in range(1, n):
            pre_dp[i] = max(pre_dp[i - 1], dp[i][1])

        max_prize = 0
        for yk in range(n - 1, -1, -1):
            x_index, prize_total = dp[yk]
            max_prize = max(max_prize, dp[yk][1] + (pre_dp[x_index - 1] if x_index > 0 else 0))

            if x_index == 0:
                break
        return max_prize


class Solution2:
    """
    参考题解：
    由于prizePositions非递减，在确定第二条线段的右端点后prizePositions[i]，
    可以通过二分查找左端点 prizePositions[i] - k 所在的index，此时i - index + 1即为第二条线段的奖品数目，
    在加上前index个数构成的最大奖品数目，即为i结尾的最优值。遍历即可。

    用dp[i]表示前i个数构成的最大奖品数目，那么dp[i+1] = max(dp[i], i - index + 1)
    """

    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0 for _ in range(n + 1)]
        result = 0

        for i in range(n):
            index = bisect.bisect_left(prizePositions, prizePositions[i] - k)
            second_result = i - index + 1
            result = max(result, dp[index] + second_result)
            dp[i + 1] = max(dp[i], second_result)
        return result


class Solution3:
    """
    参考题解：
    用dp[i]表示前i个数构成的最大奖品数目，那么dp[i+1] = max(dp[i], i - index + 1)
    用滑动窗口来指定第二个线段。
    """

    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0 for _ in range(n + 1)]
        left = 0

        result = 0
        for right, value in enumerate(prizePositions):
            while value - prizePositions[left] > k:
                left += 1
            second_result = right - left + 1
            result = max(result, second_result + dp[left])
            dp[right + 1] = max(dp[right], second_result)
        return result


if __name__ == '__main__':
    solution = Solution3

    for idx, (case_input, case_output) in enumerate([
        (([1, 1, 2, 2, 3, 3, 5], 2), 7),
        (([1, 2, 3, 4], 0), 2),
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().maximizeWin(*case_input)}')
