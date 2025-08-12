"""
Problem
-------
https://leetcode.com/problems/reverse-words-in-a-string/

Solution
--------
Use the built in Python functions for strings ``split`` to split the string,
``reversed`` to reverse the list, and ``join`` to join the list back into a
string.

Code
----

.. literalinclude:: ../solutions/medium/ReverseWordsInAString.py
    :language: python
    :lines: 31-

Test
----
>>> from ReverseWordsInAString import reverseWords
>>> reverseWords('the sky is blue')
'blue is sky the'
>>> reverseWords('  hello world  ')
'world hello'
>>> reverseWords('a good   example')
'example good a'
"""


def reverseWords(s: str) -> str:
    """Reverse the words in a string, separated by 1 space.
    """
    words = s.strip().split()
    return ' '.join(reversed(words))
