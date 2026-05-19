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
