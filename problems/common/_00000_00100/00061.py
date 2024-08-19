#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/rotate-list/description/
# ============================================================

"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {'' if not self.next else repr(self.next)}"


class Solution:
    """
    由于0 <= k <= 2 * 10**9，显然不能全部旋转一次

    每经过链表长度次的旋转回归原位，取mod后旋转
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        nodes = []
        now = head
        while now:
            nodes.append(now)
            now = now.next

        k = k % len(nodes)
        if k == 0:
            return head

        nodes[-k - 1].next = None
        nodes[-1].next = head
        return nodes[-k]


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        (([0, 1, 2], 4), [2, 0, 1]),
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        head = ListNode(i[0][0])
        pre = head
        for j in range(1, len(i[0])):
            now = ListNode((i[0][j]))
            pre.next = now
            pre = now
        print(f'	output: {solution().rotateRight(head, i[1])}')
