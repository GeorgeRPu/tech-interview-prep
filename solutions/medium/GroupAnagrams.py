"""
Problem
-------
https://leetcode.com/problems/group-anagrams

Given an array of strings ``strs``, group the anagrams together. You can
return the answer in **any order**.

 

**Example 1:**

.. container:: example-block

   **Input:** strs = ["eat","tea","tan","ate","nat","bat"]

   **Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

   **Explanation:**

   - There is no string in strs that can be rearranged to form
     ``"bat"``.
   - The strings ``"nat"`` and ``"tan"`` are anagrams as they can be
     rearranged to form each other.
   - The strings ``"ate"``, ``"eat"``, and ``"tea"`` are anagrams as
     they can be rearranged to form each other.

**Example 2:**

.. container:: example-block

   **Input:** strs = [""]

   **Output:** [[""]]

**Example 3:**

.. container:: example-block

   **Input:** strs = ["a"]

   **Output:** [["a"]]

 

**Constraints:**

- ``1 <= strs.length <= 10``\ :sup:```4```
- ``0 <= strs[i].length <= 100``
- ``strs[i]`` consists of lowercase English letters.

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
    :lines: 78-

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
