#!/usr/bin/env python
# coding=utf-8
# ============================================================
# Author: ChenBing
# ============================================================
import re
from typing import Callable
from typing import List


def create_binary_tree(
        input_array: List,
        node_constructor: Callable
):
    """
    创建二叉树
    :param input_array: 输入的二叉树数据
    :param node_constructor: 二叉树节点构造方法, 接收参数val, 返回Node, 该Node需要满足:
                             .left为左子树, .right为右子树, .val为节点值
    :return: 二叉树根节点
    """
    if not input_array:
        return None

    def _insert_node(_root, _node):
        if _root.val < _node.val:
            if _root.right:
                _insert_node(_root.right, _node)
            else:
                _root.right = _node
        else:
            if _root.left:
                _insert_node(_root.left, _node)
            else:
                _root.left = _node

    root = node_constructor(input_array[0])
    for i in range(1, len(input_array)):
        _insert_node(root, node_constructor(input_array[i]))
    return root


def create_binary_tree_for_leetcode_input(
        input_string: str,
        node_constructor: Callable,
        is_none_node: Callable = lambda x: x == 'null',
        element_to_value: Callable = lambda x: int(x),
        is_complete_bst_input: bool = False
):
    """
    创建二叉树
    :param input_string: 输入的字符串
    :param node_constructor: 二叉树节点构造方法, 接收参数val, 返回Node, 该Node需要满足:
                             .left为左子树, .right为右子树, .val为节点值
    :param is_none_node: 判断输入是否对应的None节点 (即叶子节点的left, right)
    :param element_to_value: 字符串转Node.val的方法
    :param is_complete_bst_input: 输入list是否为完全二叉树格式,
                                  若为完全二叉树, 则严格按照下标构造;
                                  若不为完全二叉树, 则输入的数据作为当前可用节点的left, right
    :return: 二叉树根节点
    """
    if not input_string:
        return None

    matcher = re.search(r'root\s*=\s*\[(.+)\]', input_string)
    if not matcher:
        return []
    input_nodes = [None if is_none_node(e.strip()) else node_constructor(element_to_value(e.strip()))
                   for e in matcher.group(1).split(',')]

    root = input_nodes[0]
    if is_complete_bst_input:
        nodes = [root]
        for i in range(1, len(input_nodes)):
            now = input_nodes[i]
            if i % 2 == 0:
                nodes[(i - 1) // 2].left = now
            else:
                nodes[(i - 1) // 2].right = now
        return root

    nodes = [root]
    nodes_index = 0
    left = True
    for i in range(1, len(input_nodes)):
        now = input_nodes[i]
        if left:
            nodes[nodes_index].left = now
            left = False
        else:
            nodes[nodes_index].right = now
            left = True
            nodes_index += 1
        if now:
            nodes.append(now)
    return root


def traverse_binary_tree(root, traverse_order: str = 'inorder') -> List:
    """
    遍历二叉树

    :param root: 二叉树根节点, .left为左子树, .right为右子树, .val为节点值
    :param traverse_order: 遍历次序, preorder先序遍历, inorder中序遍历, postorder后序遍历
    :return: 按order遍历的节点list
    """
    if not root:
        return []

    if traverse_order not in ('preorder', 'inorder', 'postorder'):
        traverse_order = 'preorder'

    nodes = []

    def _add_node(_node):
        if _node:
            nodes.append(_node)

    if traverse_order == 'preorder':
        def _preorder_traverse(_root):
            _add_node(_root)
            if _root:
                _preorder_traverse(_root.left)
                _preorder_traverse(_root.right)

        _preorder_traverse(root)
    elif traverse_order == 'inorder':
        def _inorder_traverse(_root):
            if _root:
                _inorder_traverse(_root.left)
            _add_node(_root)
            if _root:
                _inorder_traverse(_root.right)

        _inorder_traverse(root)
    else:
        def _postorder_traverse(_root):
            if _root:
                _postorder_traverse(_root.right)
            _add_node(_root)
            if _root:
                _postorder_traverse(_root.left)

        _postorder_traverse(root)
    return nodes


def traverse_binary_tree_for_leetcode_output(root) -> List:
    """
    遍历二叉树

    :param root: 二叉树根节点, .left为左子树, .right为右子树, .val为节点值
    :return: 遍历次序的node集合
    """
    if not root:
        return []
    nodes = [root]

    for e in nodes:
        if e:
            nodes.append(e.left)
            nodes.append(e.right)

    return nodes


if __name__ == '__main__':
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

        def __repr__(self):
            return str(self.val)


    test_root = create_binary_tree([9, 4, 3, 2, 5, 6, 7, 0, 8, 1], Node)
    test_nodes = traverse_binary_tree(test_root, traverse_order='postorder')

    print(test_nodes)
