"""
Problem
-------
https://leetcode.com/problems/longest-common-prefix/submissions/

Solution
--------
Iterate through each character in the shortest string and check if it is in all
other strings in ``strs``.

Test
----
>>> from LongestCommonPrefix import longest_common_prefix
>>> longest_common_prefix(['flower', 'flow', 'flight'])
'fl'
>>> longest_common_prefix(['dog', 'racecar', 'car'])
''
"""


from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """Find longest common prefix of all strings in ``strs``.
    """
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        if any(other[i] != char for other in strs):
            return shortest[:i]
    return shortest
