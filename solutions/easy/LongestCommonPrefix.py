"""
Problem
-------
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string ``""``.

 

**Example 1:**

::


   Input: strs = ["flower","flow","flight"]
   Output: "fl"

**Example 2:**

::


   Input: strs = ["dog","racecar","car"]
   Output: ""
   Explanation: There is no common prefix among the input strings.

 

**Constraints:**

- ``1 <= strs.length <= 200``
- ``0 <= strs[i].length <= 200``
- ``strs[i]`` consists of only lowercase English letters if it is
  non-empty.

Solution
--------
Iterate through each character in the shortest string and check if it is in all
other strings in ``strs``.

Code
----

.. literalinclude:: ../solutions/easy/LongestCommonPrefix.py
    :language: python
    :lines: 61-

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
