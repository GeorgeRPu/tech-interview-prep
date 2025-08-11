"""
Problem
-------
https://leetcode.com/problems/word-pattern/

Solution
--------
Split ``s`` into a list of words. The problem reduces to IsomorphicStrings but
with characters in ``pattern`` and elements in ``s``. Since ``pattern`` and
``s`` can have different lenghts, we first check that they have the same
length.

Code
----

.. literalinclude:: ../solutions/easy/WordPattern.py
    :language: python
    :lines: 30-

Test
----
>>> from WordPattern import wordPattern
>>> wordPattern('abba', 'dog cat cat dog')
True
>>> wordPattern('abba', 'dog cat cat fish')
False
>>> wordPattern('aaaa', 'dog cat cat dog')
False
"""


def wordPattern(pattern: str, s: str) -> bool:
    """Given a pattern and a string s, finds if ``s`` follows the same pattern.
    """
    words = s.split()

    if len(pattern) != len(words):
        return False

    d = {}
    d_range = set()
    for char, word in zip(pattern, words):
        if char in d:
            if d[char] != word:
                return False
        else:
            if word in d_range:
                return False
            else:
                d[char] = word
                d_range.add(word)

    return True
