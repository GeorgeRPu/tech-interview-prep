r"""
>>> from group_anagrams__character_count import groupAnagrams
>>> groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
>>> groupAnagrams([""])
[['']]
>>> groupAnagrams(["a"])
[['a']]
"""

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    counters = []
    for s in strs:
        counter = [0] * 26
        for char in s:
            counter[ord(char) - ord("a")] += 1

        counters.append((s, counter))

    groups = defaultdict(list)
    for s, counter in counters:
        groups[tuple(counter)].append(s)

    return list(groups.values())
