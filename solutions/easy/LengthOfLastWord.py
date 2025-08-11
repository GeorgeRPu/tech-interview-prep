"""
Problem
-------
https://leetcode.com/problems/length-of-last-word/

Solution
--------
Strip all the whitespace from the end of the string, then split the string by
spaces. The last element in the list is the last word in the string.

Code
----

.. literalinclude:: ../solutions/easy/LengthOfLastWord.py
    :language: python
    :lines: 28-

Test
----
>>> from LengthOfLastWord import lengthOfLastWord
>>> lengthOfLastWord('Hello World')
5
>>> lengthOfLastWord('   fly me   to   the moon  ')
4
>>> lengthOfLastWord('luffy is still joyboy')
6
"""


def lengthOfLastWord(s: str) -> int:
    """Finds the length of the last word in a string.
    """
    return len(s.strip().split(' ')[-1])
