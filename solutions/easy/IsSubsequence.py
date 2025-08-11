"""
Problem
-------
https://leetcode.com/problems/is-subsequence/

Solution
--------
If ``s`` is a subsequence of ``t``, then the characters in ``s`` should appear
in ``t`` in order. Iterate through ``t`` and check if each character in ``s``
appears in ``t`` in order.

Code
----

.. literalinclude:: ../solutions/easy/IsSubsequence.py
    :language: python
    :lines: 27-

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
