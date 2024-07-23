"""
思路:
1. r大的引爆的bomb更多, 因此从大r开始引爆
2. 若(x0-x1)**2 + (y0-y1)**2 <= r0**2, 则bomb0可以引爆bomb[1]

构造n*n的矩阵A,
当A[i][j] == 0时表示 bomb[i]不能引爆bomb[j]
当A[i][j] != 0时表示 bomb[i]能引爆bomb[j]

遍历获取最大的count
"""
import queue
import time
from typing import List


def time_cost_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'time cose: {end - start}ms')
        return result

    return wrapper


class Solution:

    @time_cost_wrapper
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if not bombs:
            return 0

        if len(bombs) == 1:
            return 1

        exist_link = False
        n = len(bombs)
        a = []
        for i in range(0, n):
            links = []
            for j in range(0, n):
                if i != j and self._can_2_bomb_link(bombs[i], bombs[j]):
                    links.append(j)
                    exist_link = True
            a.append(links)

        if not exist_link:
            return 1

        max_count = 0
        for i in range(0, n):
            current_count = 0
            visited = [0] * n
            q = queue.Queue()
            q.put(i)

            while not q.empty():
                index = q.get()
                if not visited[index]:
                    visited[index] = 1
                    current_count += 1
                    for j in a[index]:
                        if not visited[j]:
                            q.put(j)

            max_count = max(current_count, max_count)
            if max_count == n:
                return max_count
        return max_count

    def _can_2_bomb_link(self, bomb0: List[int], bomb1: List[int]) -> bool:
        return (bomb0[0] - bomb1[0]) ** 2 + (bomb0[1] - bomb1[1]) ** 2 <= bomb0[2] ** 2
