r"""
>>> from is_subsequence__two_pointers import isSubsequence
>>> isSubsequence("abc", "ahbgdc")
True
>>> isSubsequence("axc", "ahbgdc")
False
"""


def isSubsequence(s: str, t: str) -> bool:
    """Returns whether ``s`` is a subsequence of ``t``."""
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
