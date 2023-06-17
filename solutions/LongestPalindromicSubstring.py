"""
Problem
-------
https://leetcode.com/problems/longest-palindromic-substring/

Solution
--------
Any palindromic substring can have odd or even length. If the substring has odd
length, then the center of the palindrome is a single character. If the
substring has even length, then the center of the palindrome are 2 equal
characters. We iterate through ``s`` and find all odd and even centers. Given a
palindromic center, we can expand the substring by moving the start and end
indices while checking that the substring is still a palindrome. When the
palindrome exceeds the previous longest palindrome, replace the longest
plaindrome.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/LongestPalindromicSubstring.py

.. literalinclude:: ../solutions/LongestPalindromicSubstring.py
    :language: python
    :lines: 35-

Test
----
>>> from LongestPalindromicSubstring import longestPalindrome
>>> longestPalindrome('babad')
'bab'
>>> longestPalindrome('cbbd')
'bb'
"""


def longestPalindrome(s: str) -> str:
    """Return the longest palindromic substring of ``s``.
    """
    longest_substr = ''
    for i, char in enumerate(s):
        for j in range(1, 3):
            start = i
            end = i + j
            substr = s[start:end]
            while is_palindrome(substr) and in_bounds(start, end, s):
                if len(substr) > len(longest_substr):
                    longest_substr = substr

                start -= 1
                end += 1
                substr = s[start:end]

    return longest_substr


def is_palindrome(substr):
    return substr == substr[::-1]


def in_bounds(start, end, s):
    return start >= 0 and end <= len(s)
