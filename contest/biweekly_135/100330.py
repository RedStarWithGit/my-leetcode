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

# ============================================================
# Expose
# ============================================================

# ============================================================
# Common
# ============================================================

class Solution:
    def minimumLength(self, s: str) -> int:
        # 1,3,5,7,9,... => 1
        # 2,4,6,8,10,... => 2
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        result = 0
        for k in count.values():
            result += (2 if k % 2 == 0 else 1)
        return result


if __name__ == '__main__':
    print(
        # Solution().minimumLength("abaacbcbb")
        Solution().minimumLength("aa")
    )