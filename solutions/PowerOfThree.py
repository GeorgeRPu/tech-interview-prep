"""
Problem
-------
https://leetcode.com/problems/power-of-three/

Solution
--------
Note that, if :math:`n = 3^x`, :math:`n` can never be negative. For positive
:math:`n``, check if :math:`n` is divisble by 3. If it is, divide :math:`n` by
3 and check again. If it is not, then :math:`n` is not a power of 3.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/PowerOfThree.py

Test
----
>>> from PowerOfThree import isPowerOfThree
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
