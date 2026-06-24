r"""
>>> from longest_common_prefix__vertical_scan import longestCommonPrefix
>>> longestCommonPrefix(['flower', 'flow', 'flight'])
'fl'
>>> longestCommonPrefix(['dog', 'racecar', 'car'])
''
"""


def longestCommonPrefix(strs: list[str]) -> str:
    """Find longest common prefix of all strings in ``strs``."""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        if any(other[i] != char for other in strs):
            return shortest[:i]
    return shortest
