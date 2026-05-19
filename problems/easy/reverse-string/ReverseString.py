r"""
>>> from ReverseString import reverseString
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> reverseString(s)
>>> s
['o', 'l', 'l', 'e', 'h']
>>> s = ['H', 'a', 'n', 'n', 'a', 'h']
>>> reverseString(s)
>>> s
['h', 'a', 'n', 'n', 'a', 'H']
"""


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    end = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[end - i] = s[end - i], s[i]
