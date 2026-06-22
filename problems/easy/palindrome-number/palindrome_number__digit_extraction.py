r"""
>>> from palindrome_number__digit_extraction import isPalindrome
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
