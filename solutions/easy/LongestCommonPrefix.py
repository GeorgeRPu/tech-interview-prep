"""
Problem
-------
https://leetcode.com/problems/longest-common-prefix/

Solution
--------
Iterate through each character in the shortest string and check if it is in all
other strings in ``strs``.

Code
----

.. literalinclude:: ../solutions/easy/LongestCommonPrefix.py
    :language: python
    :lines: 26-

Test
----
>>> from LongestCommonPrefix import longestCommonPrefix
>>> longestCommonPrefix(['flower', 'flow', 'flight'])
'fl'
>>> longestCommonPrefix(['dog', 'racecar', 'car'])
''
"""


from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """Find longest common prefix of all strings in ``strs``.
    """
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        if any(other[i] != char for other in strs):
            return shortest[:i]
    return shortest
