"""
Problem
-------
https://leetcode.com/problems/first-unique-character-in-a-string/

Solution
--------
Use a dictionary to count the number of times each character appears in ``s``.
Iterate through the string again. The first character that has a count of 1 is
the first unique character.

Code
----

.. literalinclude:: ../solutions/easy/FirstUniqueCharacterInAString.py
    :language: python
    :lines: 31-

Test
----
>>> from FirstUniqueCharacterInAString import firstUniqChar
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
