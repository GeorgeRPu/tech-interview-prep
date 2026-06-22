r"""
>>> from power_of_three__recursive import isPowerOfThree
>>> isPowerOfThree(27)
True
>>> isPowerOfThree(0)
False
>>> isPowerOfThree(-1)
False
"""


def isPowerOfThree(n: int) -> bool:
    """Check if ``n`` is a power of 3.
    """
    if n <= 0:
        return False
    elif n == 1:
        return True
    elif n % 3 == 0:
        return isPowerOfThree(n / 3)
    else:
        return False
