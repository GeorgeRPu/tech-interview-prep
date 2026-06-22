r"""
>>> from valid_palindrome__two_pointers import isPalindrome
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
    s = ''.join(filter(str.isalnum, s))

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
