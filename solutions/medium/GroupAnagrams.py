"""
Problem
-------
https://leetcode.com/problems/group-anagrams

Solution
--------
We can check whether 2 strings are anagrams by counting the number of each
letter in a dictionary. If the 2 strings are anagrams, then the dictionaries
will be equal. For each string, check whether it is an anagram of any of the
existing groups. If so, add it to that group. Otherwise, create a new group. To
save time on dictionary creation, we store a dictionary for each group.

Code
----

.. literalinclude:: ../solutions/medium/GroupAnagrams.py
    :language: python
    :lines: 32-

Test
----
>>> from GroupAnagrams import groupAnagrams
>>> groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
>>> groupAnagrams([""])
[['']]
>>> groupAnagrams(["a"])
[['a']]
"""

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """Group ``strs`` into anagrams.
    """
    dicts = []
    groups = []
    for s in strs:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 0

        for i, group in enumerate(groups):
            if d == dicts[i]:
                groups[i].append(s)
                break
        else:
            groups.append([s])
            dicts.append(d)

    return groups
