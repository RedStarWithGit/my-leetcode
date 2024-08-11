#!/usr/bin/env python
# coding=utf-8
# ============================================================
# https://leetcode.cn/problems/implement-trie-prefix-tree/description/
# ============================================================

"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
Trie()
    初始化前缀树对象。
void insert(String word)
    向前缀树中插入字符串 word 。
boolean search(String word)
    如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix)
    如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
"""


class Node:
    def __init__(self, val=None):
        self.char_value = val
        self.finished = False
        self.next = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word:
            return

        now = self.root
        for ch in word:
            next_node = now.next.get(ch, None)
            if not next_node:
                next_node = Node(ch)
                now.next[ch] = next_node
            now = next_node
        now.finished = True

    def search(self, word: str) -> bool:
        if not word:
            return True

        now = self.root
        for ch in word:
            next_node = now.next.get(ch, None)
            if not next_node:
                return False
            now = next_node
        return now.finished

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        now = self.root
        for ch in prefix:
            next_node = now.next.get(ch, None)
            if not next_node:
                return False
            now = next_node
        return True


if __name__ == '__main__':
    solution = Trie

    for idx, (i, o) in enumerate([
        (
                (
                        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
                        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
                ),
                '[null, null, true, false, true, null, true]'
        )
    ]):
        print(f'case {idx}: {i}')
        print(f'	predict: {o}')

        print('\toutput: ', end='')
        trie = None
        for action, params in zip(i[0], i[1]):
            if action == 'Trie':
                trie = solution()
                print('null', end=', ')
            elif action == 'insert':
                trie.insert(params[0])
                print('null', end=', ')
            elif action == 'search':
                output = trie.search(params[0])
                print(output, end=', ')
            elif action == 'startsWith':
                output = trie.startsWith(params[0])
                print(output, end=', ')
        print()
