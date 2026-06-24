r"""
>>> from design_add_and_search_words_data_structure__trie_with_dfs import WordDictionary
>>> wd = WordDictionary()
>>> wd.addWord("bad"); wd.addWord("dad"); wd.addWord("mad")
>>> wd.search("pad")
False
>>> wd.search("bad")
True
>>> wd.search(".ad")
True
>>> wd.search("b..")
True
"""


class TrieNode:

    def __init__(self, char, end_of_word=False):
        self.char = char
        self.end_of_word = end_of_word
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("<SOW>")

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word)

    def _search(self, node: TrieNode, word: str) -> bool:
        if len(word) == 0:
            return node.end_of_word

        char = word[0]
        if char == ".":
            return any(
                self._search(child, word[1:])
                for child in node.children.values()
            )
        elif char not in node.children:
            return False
        else:
            return self._search(node.children[char], word[1:])
