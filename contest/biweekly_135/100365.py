#!/usr/bin/env python
# coding=utf-8
# ============================================================
# Author: ChenBing
# ============================================================
# 
# ============================================================

# ============================================================
# Import
# ============================================================

from typing import List


# ============================================================
# Expose
# ============================================================

# ============================================================
# Common
# ============================================================

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        diffs = {}
        indexes = {}
        nums_size = len(nums)
        for i in range(0, nums_size // 2):
            diff = abs(nums[i] - nums[nums_size - i - 1])
            diffs[diff] = diffs.get(diff, 0) + 1

            if diff not in indexes.keys():
                indexes[diff] = []
            indexes[diff].append(i)

        if len(diffs) == 1:
            return 0

        real = sorted(diffs.items(), key=lambda kv: kv[1], reverse=True)
        # print(real)
        # print(indexes)

        min_count = None
        for outer in range(0, len(real)):
            real_diff = real[outer][0]
            if min_count and (nums_size - real[outer][1] * 2) // 2 >= min_count:
                continue

            count = 0
            for i in range(0, len(real)):
                if i == outer:
                    continue

                diff = real[i][0]
                for index in indexes[diff]:
                    a = nums[index]
                    b = nums[nums_size - 1 - index]
                    if (0 <= real_diff + b <= k or 0 <= b - real_diff <= k
                            or 0 <= real_diff + a <= k or 0 <= a - real_diff <= k):
                        count += 1
                    else:
                        count += 2

                    if min_count and count >= min_count:
                        break
            if not min_count:
                min_count = count
            else:
                min_count = min(min_count, count)
            # print(f'use {real_diff}, count={count}, min={min_count}')
        return min_count


if __name__ == '__main__':
    print(
        Solution().minChanges([1, 0, 1, 2, 4, 3], 4),  # 2
        Solution().minChanges([0, 1, 2, 3, 3, 6, 5, 4], 6),  # 2
        Solution().minChanges([1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0], 1),  # 4
        Solution().minChanges([0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10], 10),  # 5
        Solution().minChanges([9, 2, 7, 7, 8, 9, 1, 5, 1, 9, 4, 9, 4, 7], 9),  # 4
    )
