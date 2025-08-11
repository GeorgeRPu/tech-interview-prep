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

.. literalinclude:: ../solutions/medium/LongestPalindromicSubstring.py
    :language: python
    :lines: 32-

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
    for center, char in enumerate(s):
        longest_substr = longestPalindromeAtCenter(s, center, longest_substr=longest_substr)
        longest_substr = longestPalindromeAtCenter(s, center, offset=1, longest_substr=longest_substr)

    return longest_substr


def longestPalindromeAtCenter(s, center, offset=0, longest_substr=''):
    """Return the longest palindromic substring of ``s`` centered at
    ``center``.
    """
    i = 0
    start = center - i
    end = center + i + offset
    while 0 <= start and end <= len(s):
        if s[start] != s[end - 1]:
            break
        elif 2 * i + offset > len(longest_substr):
            longest_substr = s[start:center + i + offset]

        i += 1
        start, end = getSubstringBounds(center, i, offset)

    return longest_substr


def getSubstringBounds(center, i, offset=0):
    """Calculate the start and end indices of a substring centered at
    ``center`` with radius ``i``.
    """
    return center - i, center + i + offset
