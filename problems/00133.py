#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/clone-graph/description/
# ============================================================

"""
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        val_nodes = {}
        new_node = Node(node.val, list(node.neighbors))
        val_nodes[new_node.val] = new_node
        nodes = [new_node]
        for now in nodes:
            for i in range(0, len(now.neighbors)):
                if now.neighbors[i].val not in val_nodes.keys():
                    now.neighbors[i] = Node(now.neighbors[i].val, list(now.neighbors[i].neighbors))
                    nodes.append(now.neighbors[i])
                    val_nodes[now.neighbors[i].val] = now.neighbors[i]
                else:
                    now.neighbors[i] = val_nodes[now.neighbors[i].val]
        return new_node


if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([

    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')
        solution().cloneGraph(Node(1))
