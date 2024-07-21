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
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0

        bits = bin(n ^ k)[2:]
        n_bits = bin(n)[2:]
        diff = len(bits) - len(n_bits)
        if diff > 0:
            n_bits = f"{'0' * diff}{n_bits}"
        elif diff < 0:
            bits = f"{'0' * (-diff)}{bits}"
        # print(f'bits: {bits}')
        # print(f'n_bits: {n_bits}')

        count = 0
        for i in range(0, len(bits)):
            if bits[i] == '1':
                if n_bits[i] != '1':
                    return -1
                count += 1
        return count


if __name__ == '__main__':
    print(
        Solution().minChanges(13, 4),
        Solution().minChanges(21, 21),
        Solution().minChanges(14, 13),
    )
