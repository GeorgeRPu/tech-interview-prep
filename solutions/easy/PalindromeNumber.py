r"""
Problem
-------
https://leetcode.com/problems/palindrome-number/

Given an integer ``x``, return ``true`` *if* ``x`` *is a* palindrome\ *,
and* ``false`` *otherwise*.

 

**Example 1:**

::


   Input: x = 121
   Output: true
   Explanation: 121 reads as 121 from left to right and from right to left.

**Example 2:**

::


   Input: x = -121
   Output: false
   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

::


   Input: x = 10
   Output: false
   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

**Constraints:**

- ``-2``\ :sup:```31```\ `` <= x <= 2``\ :sup:```31```\ `` - 1``

 

**Follow up:** Could you solve it without converting the integer to a
string?

Solution
--------
Extract the digits from a number and store them in a list ``digits``. Then
compare the list with its reverse ``digits[::-1]`` to check if the number is a
palindrome.

Pattern
-------
Math

Code
----

.. literalinclude:: ../solutions/easy/PalindromeNumber.py
    :language: python
    :lines: 78-

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
