r"""
>>> from first_unique_character_in_a_string__hash_map import firstUniqChar
>>> firstUniqChar('leetcode')
0
>>> firstUniqChar('loveleetcode')
2
>>> firstUniqChar('aabb')
-1
"""


def firstUniqChar(s: str) -> int:
    """Returns the first character in ``s`` that doens't repeat.
    """
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1
