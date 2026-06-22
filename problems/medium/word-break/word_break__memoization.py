r"""
>>> from word_break__memoization import wordBreak
>>> wordBreak("leetcode", ["leet", "code"])
True
>>> wordBreak("applepenapple", ["apple", "pen"])
True
>>> wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
False
"""

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)

    memo = {len(s): True}

    def word_break(i):
        if i in memo:
            return memo[i]

        result = False
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in wordDict:
                result = result or word_break(j)

        memo[i] = result
        return result

    return word_break(0)
