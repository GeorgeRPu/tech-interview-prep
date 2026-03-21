"""
Problem
-------
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings ``needle`` and ``haystack``, return the index of the
first occurrence of ``needle`` in ``haystack``, or ``-1`` if ``needle``
is not part of ``haystack``.

 

**Example 1:**

::


   Input: haystack = "sadbutsad", needle = "sad"
   Output: 0
   Explanation: "sad" occurs at index 0 and 6.
   The first occurrence is at index 0, so we return 0.

**Example 2:**

::


   Input: haystack = "leetcode", needle = "leeto"
   Output: -1
   Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

**Constraints:**

- ``1 <= haystack.length, needle.length <= 10``\ :sup:```4```
- ``haystack`` and ``needle`` consist of only lowercase English
  characters.

Solution
--------
Iterate through each character in ``haystack`` and check if the substring
``haystack[i:i + len(needle)]`` is equal to ``needle``.

Pattern
-------
Two Pointers, String, String Matching

Code
----

.. literalinclude:: ../solutions/easy/FindTheIndexOfTheFirstOccurrenceInAString.py
    :language: python
    :lines: 65-

Test
----
>>> from FindTheIndexOfTheFirstOccurrenceInAString import strStr
>>> strStr('hello', 'll')
2
>>> strStr('aaaaa', 'bba')
-1
"""


def strStr(haystack: str, needle: str) -> int:
    """Find the first occurrence of ``needle`` in ``haystack``.
    """
    for i, char in enumerate(haystack):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1
