"""
Problem
-------
https://leetcode.com/problems/isomorphic-strings/

Solution
--------
Observe that if two strings are isomorphic, then the first character in ``s``
must map to the first character in ``t``. Similarly, for the second character
to the last character. If the 2 strings are isomorphic, this is a one-to-one
map. We can use a dictionary to store the one-to-one map from ``s`` to ``t``.
Iterate through the characters in ``s`` and ``t`` at the same time. If the
``s`` character is not in the dictionary, then add it to the dictionary and to
the range set. Check injectivity, that the ``t`` character is not in the range
set. If the character in ``s`` is in the dictionary, then check if it maps to
the character in ``t``.

Code
----

.. literalinclude:: ../solutions/easy/IsomorphicStrings.py
    :language: python
    :lines: 35-

Test
----
>>> from IsomorphicStrings import isIsomorphic
>>> isIsomorphic('egg', 'add')
True
>>> isIsomorphic('foo', 'bar')
False
>>> isIsomorphic('paper', 'title')
True
"""


def isIsomorphic(s: str, t: str) -> bool:
    """Checks if 2 strings are isomorphic.
    """
    d = {}
    d_range = set()
    for s_char, t_char in zip(s, t):
        if s_char in d:
            if d[s_char] != t_char:
                return False
        else:
            if t_char in d_range:
                return False
            else:
                d[s_char] = t_char
                d_range.add(t_char)

    return True
