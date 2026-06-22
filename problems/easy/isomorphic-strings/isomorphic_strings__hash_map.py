r"""
>>> from isomorphic_strings__hash_map import isIsomorphic
>>> isIsomorphic('egg', 'add')
True
>>> isIsomorphic('foo', 'bar')
False
>>> isIsomorphic('paper', 'title')
True
"""


def isIsomorphic(s: str, t: str) -> bool:
    """Checks if 2 strings are isomorphic.
    """
    d = {}
    d_range = set()
    for s_char, t_char in zip(s, t):
        if s_char in d:
            if d[s_char] != t_char:
                return False
        else:
            if t_char in d_range:
                return False
            else:
                d[s_char] = t_char
                d_range.add(t_char)

    return True
