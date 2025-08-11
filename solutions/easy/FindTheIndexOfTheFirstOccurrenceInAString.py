"""
Problem
-------
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Solution
--------
Iterate through each character in ``haystack`` and check if the substring
``haystack[i:i + len(needle)]`` is equal to ``needle``.

Code
----

.. literalinclude:: ../solutions/easy/FindTheIndexOfTheFirstOccurrenceInAString.py
    :language: python
    :lines: 26-

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
