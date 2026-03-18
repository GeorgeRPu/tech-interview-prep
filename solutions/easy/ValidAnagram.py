"""
Problem
-------
https://leetcode.com/problems/valid-anagram/

Given two strings ``s`` and ``t``, return ``true`` if ``t`` is an
anagram of ``s``, and ``false`` otherwise.

 

**Example 1:**

.. container:: example-block

   **Input:** s = "anagram", t = "nagaram"

   **Output:** true

**Example 2:**

.. container:: example-block

   **Input:** s = "rat", t = "car"

   **Output:** false

 

**Constraints:**

- ``1 <= s.length, t.length <= 5 * 10``\ :sup:```4```
- ``s`` and ``t`` consist of lowercase English letters.

 

**Follow up:** What if the inputs contain Unicode characters? How would
you adapt your solution to such a case?

Solution
--------
For two strings to be anagrams, they must have the same number of each
character. We can track the occurrences of each character in a dictionary,
incrementing for ``s`` and decrementing for ``t``. If the dictionary only
contanins 0's, then ``s`` and ``t`` are anagrams.

Code
----

.. literalinclude:: ../solutions/easy/ValidAnagram.py
    :language: python
    :lines: 63-

Test
----
>>> from ValidAnagram import isAnagram
>>> isAnagram('anagram', 'nagaram')
True
>>> isAnagram('rat', 'car')
False
"""


def isAnagram(s: str, t: str) -> bool:
    """Checks if ``s`` and ``t`` are anagrams of each other.
    """
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
