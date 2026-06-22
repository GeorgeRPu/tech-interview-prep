r"""
>>> from permutation_in_string__sliding_window import checkInclusion
>>> checkInclusion("ab", "eidbaooo")
True
>>> checkInclusion("ab", "eidboaoo")
False
"""

from collections import Counter, defaultdict
from collections import defaultdict

def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    if n > len(s2):
        return False

    s1_multiset = Counter(s1)
    window_multiset = defaultdict(int)

    for i in range(n):
        window_multiset[s2[i]] += 1

    for key, val in s1_multiset.items():
        if window_multiset[key] != val:
            break
    else:
        return True

    for i in range(n, len(s2)):
        window_multiset[s2[i]] += 1
        window_multiset[s2[i - n]] -= 1

        for key, val in s1_multiset.items():
            if window_multiset[key] != val:
                break
        else:
            return True

    return False
