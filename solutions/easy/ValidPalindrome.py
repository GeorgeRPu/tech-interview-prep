"""
Problem
-------
https://leetcode.com/problems/valid-palindrome/

A phrase is a **palindrome** if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters, it
reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string ``s``, return ``true`` *if it is a* **palindrome**\ *,
or* ``false`` *otherwise*.

 

**Example 1:**

::


   Input: s = "A man, a plan, a canal: Panama"
   Output: true
   Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**

::


   Input: s = "race a car"
   Output: false
   Explanation: "raceacar" is not a palindrome.

**Example 3:**

::


   Input: s = " "
   Output: true
   Explanation: s is an empty string "" after removing non-alphanumeric characters.
   Since an empty string reads the same forward and backward, it is a palindrome.

 

**Constraints:**

- ``1 <= s.length <= 2 * 10``\ :sup:```5```
- ``s`` consists only of printable ASCII characters.

Solution
--------
First, we convert ``s`` to all lowercase. Rather than remove all
non-alphanumeric characters, we can ignore them when checking if ``s`` is a
palindrome. We do this by using two pointers ``i`` and ``j`` at the beginning
of ``s`` and at the end of ``s``. When both pointers are on non-alphanumeric
characters, move them inwards.

Pattern
-------
Two Pointers, String

Code
----

.. literalinclude:: ../solutions/easy/ValidPalindrome.py
    :language: python
    :lines: 84-

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
