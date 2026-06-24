r"""
>>> from valid_anagram__hash_map import isAnagram
>>> isAnagram('anagram', 'nagaram')
True
>>> isAnagram('rat', 'car')
False
"""


def isAnagram(s: str, t: str) -> bool:
    """Checks if ``s`` and ``t`` are anagrams of each other."""
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    for char in t:
        if char in d:
            d[char] -= 1
        else:
            return False
    return all(count == 0 for char, count in d.items())
