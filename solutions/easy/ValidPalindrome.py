"""
Problem
-------
https://leetcode.com/problems/valid-palindrome/

Solution
--------
First, we convert ``s`` to all lowercase. Rather than remove all
non-alphanumeric characters, we can ignore them when checking if ``s`` is a
palindrome. We do this by using two pointers ``i`` and ``j`` at the beginning
of ``s`` and at the end of ``s``. When both pointers are on non-alphanumeric
characters, move them inwards.

Code
----

.. literalinclude:: ../solutions/easy/ValidPalindrome.py
    :language: python
    :lines: 33-

Test
----
>>> from ValidPalindrome import isPalindrome
>>> isPalindrome('A man, a plan, a canal: Panama')
True
>>> isPalindrome('race a car')
False
>>> isPalindrome(' ')
True
>>> isPalindrome('0P')
False
"""


def isPalindrome(s: str) -> bool:
    """Check if ``s`` is a palindrome, ignoring non-alphanumeric characters.
    """
    s = s.lower()

    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
