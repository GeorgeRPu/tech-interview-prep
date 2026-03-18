"""
Problem
-------
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string ``s``, find the **first** non-repeating character in it
and return its index. If it **does not** exist, return ``-1``.

 

**Example 1:**

.. container:: example-block

   **Input:** s = "leetcode"

   **Output:** 0

   **Explanation:**

   The character ``'l'`` at index 0 is the first character that does not
   occur at any other index.

**Example 2:**

.. container:: example-block

   **Input:** s = "loveleetcode"

   **Output:** 2

**Example 3:**

.. container:: example-block

   **Input:** s = "aabb"

   **Output:** -1

 

**Constraints:**

- ``1 <= s.length <= 10``\ :sup:```5```
- ``s`` consists of only lowercase English letters.

Solution
--------
Use a dictionary to count the number of times each character appears in ``s``.
Iterate through the string again. The first character that has a count of 1 is
the first unique character.

Code
----

.. literalinclude:: ../solutions/easy/FirstUniqueCharacterInAString.py
    :language: python
    :lines: 72-

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
