r"""
>>> from implement_trie_prefix_tree__hash_map_children import Trie
>>> t = Trie()
>>> t.insert("apple")
>>> t.search("apple")
True
>>> t.search("app")
False
>>> t.startsWith("app")
True
>>> t.insert("app")
>>> t.search("app")
True
"""


class TrieNode:

    def __init__(self, char, end_of_word=False):
        self.char = char
        self.end_of_word = end_of_word
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode("<start_of_word>")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
