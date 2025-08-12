"""
Problem
-------
https://leetcode.com/problems/palindrome-number/

Solution
--------
Extract the digits from a number and store them in a list ``digits``. Then
compare the list with its reverse ``digits[::-1]`` to check if the number is a
palindrome.

Code
----

.. literalinclude:: ../solutions/easy/PalindromeNumber.py
    :language: python
    :lines: 31-

Test
----
>>> from PalindromeNumber import isPalindrome
>>> isPalindrome(121)
True
>>> isPalindrome(-121)
False
>>> isPalindrome(10)
False
"""


def isPalindrome(x: int) -> bool:
    """Check if a number is a palindrome.
    """
    if x < 0:
        return False

    digits = []
    while x > 0:
        digit = x % 10
        x //= 10
        digits.append(digit)

    return digits == digits[::-1]
