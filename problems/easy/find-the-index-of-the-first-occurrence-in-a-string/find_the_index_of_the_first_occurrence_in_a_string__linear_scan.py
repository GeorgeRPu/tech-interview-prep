r"""
>>> from find_the_index_of_the_first_occurrence_in_a_string__linear_scan import strStr
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
