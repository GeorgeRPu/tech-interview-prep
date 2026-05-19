r"""
>>> from FindTheIndexOfTheFirstOccurrenceInAString import strStr
>>> strStr('hello', 'll')
2
>>> strStr('aaaaa', 'bba')
-1
"""


def strStr(haystack: str, needle: str) -> int:
    """Find the first occurrence of ``needle`` in ``haystack``.
    """
    for i, char in enumerate(haystack):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1
