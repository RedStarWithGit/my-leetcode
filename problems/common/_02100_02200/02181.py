#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/merge-nodes-in-between-zeros/description/?envType=daily-question&envId=2024-09-02
# ============================================================

"""
给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 Node.val == 0 。

对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 0 移除，
修改后的链表不应该含有任何 0 。

返回修改后链表的头节点 head 。
"""
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__() if self.next else ''}"

    @staticmethod
    def from_list(values: List[int]):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for v in values[1:]:
            current.next = ListNode(v)
            current = current.next
        return head


class Solution:
    """
    遍历合并即可
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = None
        new_current = None

        current = head.next
        current_value = 0
        while current:
            if current.val == 0:
                if current_value > 0:
                    if not new_current:
                        new_current = ListNode(current_value)
                        new_head = new_current
                    else:
                        new_current.next = ListNode(current_value)
                        new_current = new_current.next

                    current_value = 0
            else:
                current_value += current.val
            current = current.next
        return new_head


class Solution2:
    """
    在原链表上修改
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_node = head
        traverse_node = head.next

        while traverse_node:
            if traverse_node.val == 0:
                if traverse_node.next:
                    sum_node = sum_node.next
                    sum_node.val = 0
                else:
                    sum_node.next = None
            else:
                sum_node.val += traverse_node.val
            traverse_node = traverse_node.next

        return head


if __name__ == '__main__':
    solution = Solution2

    for idx, (case_input, case_output) in enumerate([
        ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
        ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4])
    ]):
        print(f'case {idx}: {case_input}')
        print(f'	predict: {case_output}')
        print(f'	output: {solution().mergeNodes(ListNode.from_list(case_input))}')
