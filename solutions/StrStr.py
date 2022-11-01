"""
Problem
-------
https://leetcode.com/problems/implement-strstr/

Solution
--------
Iterate through each character in ``haystack`` and check if the substring
``haystack[i:i + len(needle)]`` is equal to ``needle``.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/StrStr.py

Test
----
>>> from StrStr import strStr
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
