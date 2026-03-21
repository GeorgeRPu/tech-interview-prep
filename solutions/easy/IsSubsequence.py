"""
Problem
-------
https://leetcode.com/problems/is-subsequence/

Given two strings ``s`` and ``t``, return ``true`` *if* ``s`` *is a*
**subsequence** *of* ``t``\ *, or* ``false`` *otherwise*.

A **subsequence** of a string is a new string that is formed from the
original string by deleting some (can be none) of the characters without
disturbing the relative positions of the remaining characters. (i.e.,
``"ace"`` is a subsequence of
``"``\ *``a``*\ ``b``\ *``c``*\ ``d``\ *``e``*\ ``"`` while ``"aec"`` is
not).

 

**Example 1:**

::

   Input: s = "abc", t = "ahbgdc"
   Output: true

**Example 2:**

::

   Input: s = "axc", t = "ahbgdc"
   Output: false

 

**Constraints:**

- ``0 <= s.length <= 100``
- ``0 <= t.length <= 10``\ :sup:```4```
- ``s`` and ``t`` consist only of lowercase English letters.

 

**Follow up:** Suppose there are lots of incoming ``s``, say
``s``\ :sub:```1```\ ``, s``\ :sub:```2```\ ``, ..., s``\ :sub:```k```
where ``k >= 10``\ :sup:```9```, and you want to check one by one to see
if ``t`` has its subsequence. In this scenario, how would you change
your code?

Solution
--------
If ``s`` is a subsequence of ``t``, then the characters in ``s`` should appear
in ``t`` in order. Iterate through ``t`` and check if each character in ``s``
appears in ``t`` in order.

Pattern
-------
Two Pointers, String, Dynamic Programming

Code
----

.. literalinclude:: ../solutions/easy/IsSubsequence.py
    :language: python
    :lines: 75-

Test
----
>>> from IsSubsequence import isSubsequence
>>> isSubsequence("abc", "ahbgdc")
True
>>> isSubsequence("axc", "ahbgdc")
False
"""


def isSubsequence(s: str, t: str) -> bool:
    """Returns whether ``s`` is a subsequence of ``t``.
    """
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
