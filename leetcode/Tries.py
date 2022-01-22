from __future__ import annotations
from typing import List, Optional

"""
Problem
-------
https://www.hackerrank.com/challenges/ctci-contacts/problem

Solution
--------
https://www.youtube.com/watch?v=zIjfhVPRZCg

TL;DR A trie is a tree filled such that each node is a character and successive
characters in words are descendents. Tries can be used for dictionary
autocompletion. By scanning descendant branches, we can list all words that
start with a given substring. The root is a special start of sequence (SOS)
character and the ends of words are denoted using a special end of sequence
character (EOS).

                  l - e - EOS
                /
SOS - a - p - p - EOS
        \
          x - e - EOS
"""

SOS_char = '<'
EOS_char = '>'


class Node:

    def __init__(self, char: str):
        self.char: str = char
        self.children: List[Node] = []

    def add_child(self, node: Node):
        self.children.append(node)

    def get_child(self, char) -> Optional[Node]:
        for child in self.children:
            if char == child.char:
                return child
        return None

    def descendant_strings(self, string: str):
        strings: List[str] = []
        for child in self.children:
            if child.char == EOS_char:
                strings.append(string + self.char)
            else:
                strings.extend(child.descendant_strings(string + self.char))
        return strings


class Trie:

    def __init__(self):
        self.root = Node(SOS_char)

    def add(self, string: str):
        node = self.root
        for char in string:
            child = node.get_child(char)
            if child is not None:
                node = child
            else:
                new_node = Node(char)
                node.add_child(new_node)
                node = new_node
        EOS = Node(EOS_char)
        node.add_child(EOS)

    def strings_starting_with(self, string: str) -> List[str]:
        # loop to end of string
        node = self.root
        for char in string:
            # check that path can continue
            child = node.get_child(char)
            if child is not None:
                node = child
            else:
                return []
        return node.descendant_strings(string[:-1])


trie = Trie()
trie.add('apple')
trie.add('axiom')
trie.add('animal')
trie.add('bees')
print(trie.strings_starting_with(''))
