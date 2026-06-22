r"""
>>> from group_anagrams__character_count import groupAnagrams
>>> groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
>>> groupAnagrams([""])
[['']]
>>> groupAnagrams(["a"])
[['a']]
"""

from collections import Counter
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """Group ``strs`` into anagrams.
    """
    dicts = []
    groups = []
    for s in strs:
        d = Counter(s)

        for i, group in enumerate(groups):
            if d == dicts[i]:
                groups[i].append(s)
                break
        else:
            groups.append([s])
            dicts.append(d)

    return groups
