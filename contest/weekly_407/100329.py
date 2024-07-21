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
from typing import Tuple


# ============================================================
# Expose
# ============================================================

# ============================================================
# Common
# ============================================================

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        if not nums and not target:
            return 0

        diffs = [nums[i] - target[i] for i in range(0, len(nums))]
        # print(nums)
        # print(target)
        # print(diffs)
        return self.count(diffs)

    def count(self, diffs: List[int]) -> int:
        result = 0
        split_diffs = self.split_diffs(diffs)
        i = 0
        while True:
            if i >= len(split_diffs):
                break

            each_diffs = split_diffs[i]
            r, new_split_diffs = self.count_one_split(each_diffs)
            result += r
            split_diffs.extend(new_split_diffs)

            i += 1
        return result

    def count_one_split(self, diffs: List[int]) -> Tuple[int, List[List[int]]]:
        # same sign and no zero in diffs
        result = 0
        if diffs[0] > 0:
            v = min(diffs)
            result += v
            diffs = [e - v for e in diffs]
        else:
            v = max(diffs)
            result -= v
            diffs = [e - v for e in diffs]
        return result, self.split_diffs(diffs)

    def split_diffs(self, diffs: List[int]) -> List[List[int]]:
        results = []

        current = []
        for i in range(0, len(diffs)):
            if diffs[i] == 0:
                if current:
                    results.append(current)
                    current = []
            elif diffs[i] > 0:
                if current:
                    if current[0] > 0:
                        current.append(diffs[i])
                    else:
                        results.append(current)
                        current = [diffs[i]]
                else:
                    current.append(diffs[i])
            else:  # < 0
                if current:
                    if current[0] > 0:
                        results.append(current)
                        current = [diffs[i]]
                    else:
                        current.append(diffs[i])
                else:
                    current.append(diffs[i])
        if current:
            results.append(current)
        return results


if __name__ == '__main__':
    print(
        Solution().minimumOperations(nums=[3, 5, 1, 2], target=[4, 6, 2, 4]),
        Solution().minimumOperations(nums=[1, 3, 2], target=[2, 1, 4]),
    )
