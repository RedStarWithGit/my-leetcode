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
    def maxOperations(self, s: str) -> int:
        count = 0
        before = 0
        s_len = len(s)
        i = 0
        while True:
            if i + 1 >= s_len:
                break

            if s[i] == '1':
                if s[i + 1] != '0':
                    before += 1
                else:
                    found = False
                    for j in range(i + 2, s_len):
                        if s[j] == '1':
                            count += 1
                            count += before
                            before += 1
                            i = j - 1
                            found = True
                            break
                    if not found:
                        count += 1
                        count += before
                        break
            i += 1
        return count


if __name__ == '__main__':
    print(
        Solution().maxOperations('1001101'),
        Solution().maxOperations('00111'),
        Solution().maxOperations('110'),
    )
