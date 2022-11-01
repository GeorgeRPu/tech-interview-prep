from __future__ import annotations

__doc__ = """
Problem
-------
https://www.hackerrank.com/challenges/ctci-contacts/problem

Solution
--------
https://www.youtube.com/watch?v=zIjfhVPRZCg

A trie is a tree filled such that each node is a character and successive
characters in words are descendents. Tries can be used for dictionary
autocompletion. By scanning descendant branches, we can list all words that
start with a given substring. The root is a special start of sequence (SOS)
character and the ends of words are denoted using a special end of sequence
character (EOS). ::

                    l - e - EOS
                   /
    SOS - a - p - p - EOS
           \\
            x - e - EOS

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/Tries.py

Test
----
>>> from Tries import Trie
>>> trie = Trie()
>>> trie.add('apple')
>>> trie.add('axiom')
>>> trie.add('animal')
>>> trie.add('bees')
>>> trie.strings_starting_with('a')
['apple', 'axiom', 'animal']
>>> trie.strings_starting_with('b')
['bees']
"""

from typing import List, Optional

SOS_char = '<'
EOS_char = '>'


class TrieNode:
    """Node in the trie.
    """

    def __init__(self, char: str):
        self.char: str = char
        self.children: List[TrieNode] = []

    def add_child(self, node: TrieNode):
        self.children.append(node)

    def get_child(self, char) -> Optional[TrieNode]:
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
    """Implemented as a n-ary tree of nodes.
    """

    def __init__(self):
        self.root = TrieNode(SOS_char)

    def add(self, string: str):
        node = self.root
        for char in string:
            child = node.get_child(char)
            if child is not None:
                node = child
            else:
                new_node = TrieNode(char)
                node.add_child(new_node)
                node = new_node
        EOS = TrieNode(EOS_char)
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
