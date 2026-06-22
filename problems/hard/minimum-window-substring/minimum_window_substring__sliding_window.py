r"""
>>> from minimum_window_substring__sliding_window import minWindow
>>> minWindow("ADOBECODEBANC", "ABC")
'BANC'
>>> minWindow("a", "a")
'a'
>>> minWindow("a", "aa")
''
"""

from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    left = 0
    right = 0

    diffs = defaultdict(int)
    for char in t:
        diffs[char] -= 1

    substr = ""
    while right < len(s):
        diffs[s[right]] += 1
        right += 1

        while all([d >= 0 for d in diffs.values()]):
            if substr == "":
                substr = s[left:right]
            elif len(substr) > right - left:
                substr = s[left:right]

            diffs[s[left]] -= 1
            left += 1

    return substr
