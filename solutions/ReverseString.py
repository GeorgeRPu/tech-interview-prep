"""
Problem
-------
https://leetcode.com/problems/reverse-string/

Solution
--------
Let :math:`n` be the length of the input list ``s``. Let ``end = n - 1``. We
can reverse the list by swapping the outermost elements, moving inwards. ::

    s[i], s[end - i] = s[end - i], s[i]

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/ReverseString.py

.. literalinclude:: ../solutions/ReverseString.py
    :language: python
    :lines: 35-

Test
----
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
