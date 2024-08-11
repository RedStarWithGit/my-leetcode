#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/falling-squares/description/
# ============================================================
"""
在二维平面上的 x 轴上，放置着一些方块。

给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：
第 i 个方块边长为 sideLengthi ，其左侧边与 x 轴上坐标点 lefti 对齐。

每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到
另一个正方形的顶边 或者是 x 轴上 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。
一旦着陆，它就会固定在原地，无法移动。

在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。

返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。
"""

from collections import deque
from typing import List


class Solution:
    """
    每一个方块positions[i] = [left, length]在输入时就已经可以确定x的覆盖区间为：
        x0 = left
        x1 = left + length
    覆盖区间为[x0, x1]
    方块落下前，此区间的最大高度为height；方块落下后，此区间的最大高度为height + length

    每方块落下，检测已落下方块是否会重叠，若重叠，新方块的height增加重叠区域的最高height；
    显然当存在高的height重叠区域时，无需再比较低的height重叠区域。
    为减少比较次数，维护一个height降序的已落下方块序列(x0, x1, h)。

    关于重叠区域的判断：已落下方块=(x0, x1)，新落下方块=(new_x0, new_x1)
        不重叠的判断：new_x1 <= x0 or new_x0 >= x1
        重叠取反即可：new_x1 > x0 and new_x0 < x1
    """

    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        squares = deque()
        # (x0, x1, h)
        squares.append((positions[0][0], positions[0][0] + positions[0][1], positions[0][1]))
        max_height = positions[0][1]
        results = [max_height]

        for i in range(1, len(positions)):
            position = positions[i]
            x0 = position[0]
            x1 = position[0] + position[1]
            h = position[1]

            # query overlap
            for square in squares:
                if x0 < square[1] and x1 > square[0]:
                    h = h + square[2]
                    break
            # insert new square
            inserted = False
            for j in range(len(squares)):
                if squares[j][2] < h:
                    squares.insert(j, (x0, x1, h))
                    inserted = True
                    break
            if not inserted:
                squares.append((x0, x1, h))
            max_height = max(h, max_height)
            results.append(max_height)
        return results


class _TreeNode(object):
    def __init__(self, left_scope: int, right_scope: int):
        self.val = 0
        self.left_scope = left_scope
        self.right_scope = right_scope
        self.mid = (self.left_scope + self.right_scope) // 2
        self.left = None
        self.right = None
        self.lazy_val = 0

    def __repr__(self):
        return f"[{self.left_scope, self.right_scope}]={self.val}"


class _SegmentTree(object):
    def __init__(self, left: int, right: int):
        self.root = _TreeNode(left, right)

    def query_scope(self, left: int, right: int):
        return self.__query_scope_internal(left, right, self.root)

    def __query_scope_internal(self, left: int, right: int, node: _TreeNode):
        if not node:
            return 0
        if node.left_scope >= left and node.right_scope <= right:
            return node.val

        self.__push_down(node)
        left_val = 0
        if left <= node.mid:
            left_val = self.__query_scope_internal(left, right, node.left)
        right_val = 0
        if right > node.mid:
            right_val = self.__query_scope_internal(left, right, node.right)
        return max(left_val, right_val)

    def update_scope(self, val: int, left: int, right: int):
        self.__update_scope_internal(val, left, right, self.root)

    def __update_scope_internal(self, val: int, left: int, right: int, node: _TreeNode):
        if left > right:
            return

        if node.left_scope >= left and node.right_scope <= right:
            node.val = val
            node.lazy_val = val
            return

        self.__push_down(node)
        if left <= node.mid:
            self.__update_scope_internal(val, left, right, node.left)
        if right > node.mid:
            self.__update_scope_internal(val, left, right, node.right)
        self.__push_up(node)

    def __push_up(self, node: _TreeNode):
        """
        修改子节点后需要更新当前节点值
        """
        node.val = max(node.left.val, node.right.val)

    def __push_down(self, node: _TreeNode):
        """
        当需要访问子节点时，在访问前设置val
        """
        if not node.left:
            node.left = _TreeNode(node.left_scope, node.mid)
        if not node.right:
            node.right = _TreeNode(node.mid + 1, node.right_scope)

        if node.lazy_val:
            node.left.val = node.lazy_val
            node.left.lazy_val = node.lazy_val
            node.right.val = node.lazy_val
            node.right.lazy_val = node.lazy_val
            node.lazy_val = 0


class Solution2:
    """
    线段树，每个方块落下后，查询此方块区间的最大值后修改更新
    """

    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        tree = _SegmentTree(1, 10 ** 9)
        max_height = positions[0][1]
        heights = [max_height]
        tree.update_scope(positions[0][1], positions[0][0], positions[0][0] + positions[0][1] - 1)
        from helper.tree import traverse_binary_tree
        print(traverse_binary_tree(tree.root, traverse_order='preorder'))

        for i in range(1, len(positions)):
            position = positions[i]
            x = position[0]
            h = position[1]
            y = x + h - 1
            new_height = tree.query_scope(x, y) + h
            tree.update_scope(new_height, x, y)
            max_height = max(max_height, new_height)
            heights.append(max_height)

            from helper.tree import traverse_binary_tree
            print(traverse_binary_tree(tree.root, traverse_order='preorder'))
        return heights


if __name__ == '__main__':
    solution = Solution2

    for idx, (i, o) in enumerate([
        ([[4, 6], [4, 2], [4, 3]], [6, 8, 11]),
        ([[1, 5], [2, 2], [7, 5]], [5, 7, 7]),
        ([[1, 2], [2, 3], [6, 1]], [2, 5, 5]),
        ([[100, 100], [200, 100]], [100, 100]),
        ([[1, 2], [1, 3]], [2, 5])
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        print(f'\toutput: {solution().fallingSquares(i)}')
