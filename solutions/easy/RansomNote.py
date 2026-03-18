"""
Problem
-------
https://leetcode.com/problems/ransom-note/description/

Given two strings ``ransomNote`` and ``magazine``, return ``true`` *if*
``ransomNote`` *can be constructed by using the letters from*
``magazine`` *and* ``false`` *otherwise*.

Each letter in ``magazine`` can only be used once in ``ransomNote``.

 

**Example 1:**

::

   Input: ransomNote = "a", magazine = "b"
   Output: false

**Example 2:**

::

   Input: ransomNote = "aa", magazine = "ab"
   Output: false

**Example 3:**

::

   Input: ransomNote = "aa", magazine = "aab"
   Output: true

 

**Constraints:**

- ``1 <= ransomNote.length, magazine.length <= 10``\ :sup:```5```
- ``ransomNote`` and ``magazine`` consist of lowercase English letters.

Solution
--------
Track the number of times each letter appears in the magazine. Then, when the
letter appears in the ransom note, decrement the count. If the count is ever
negative, then the ransom note cannot be constructed from the magazine. A small
optimization is to initialize the counter dictionary with all letters in the
alphabet.

Code
----

.. literalinclude:: ../solutions/easy/RansomNote.py
    :language: python
    :lines: 69-

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
