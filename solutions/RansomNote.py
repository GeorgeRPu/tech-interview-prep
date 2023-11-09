"""
Problem
-------
https://leetcode.com/problems/ransom-note/description/

Solution
--------
Track the number of times each letter appears in the magazine. Then, when the
letter appears in the ransom note, decrement the count. If the count is ever
negative, then the ransom note cannot be constructed from the magazine. A small
optimization is to initialize the counter dictionary with all letters in the
alphabet.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/RansomNote.py

.. literalinclude:: ../solutions/RansomNote.py
    :language: python
    :lines: 34-

Test
----
>>> from RansomNote import canConstruct
>>> canConstruct("a", "b")
False
>>> canConstruct("aa", "ab")
False
>>> canConstruct("aa", "aab")
True
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """Checks if ``ransomNote`` can be constructed from ``magazine`` by cutting
    and gluing letters.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    counter = {letter: 0 for letter in letters}
    for char in magazine:
        counter[char] += 1

    for char in ransomNote:
        counter[char] -= 1

    for char, count in counter.items():
        if counter[char] < 0:
            return False

    return True
