"""
Problem
-------
https://leetcode.com/problems/reverse-integer/

Solution
--------
Extract the sign of ``x``. We can use modulus and division to get the digits of
``x``. Reverse the list of digits. Then check that the digits are in the range
:math:`[2^{31} - 1, -2^{31}]`. If so, calculate the reversed integer using
the expansion

.. math::

    r = \\sum_{i=0}^{n-1} 10^i d_i.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/ReverseInteger.py

.. literalinclude:: ../solutions/ReverseInteger.py
    :language: python
    :lines: 30-

Test
----
>>> from ReverseInteger import reverse
>>> reverse(123)
321
>>> reverse(-123)
-321
>>> reverse(120)
21
"""


def reverse(x: int) -> int:
    sign = 1 if x > 0 else -1
    x = sign * x

    digits = []
    while x > 0:
        remainder = x % 10
        digits.append(remainder)
        x = x // 10

    digits = digits[::-1]

    if too_large(sign, digits):
        return 0
    else:
        r = 0
        for i, digit in enumerate(digits):
            r += digit * 10**i
        return sign * r


def too_large(sign, digits):
    if len(digits) < 10:
        return False

    if len(digits) > 10:
        return True

    tl = False
    limit = 2**31 - 1 if sign == 1 else 2**31
    for digit in enumerate(digits):
        limit_digit = limit % 10
        if digit > limit_digit:
            tl = True
        elif digit < limit_digit:
            tl = False

        limit = limit // 10

    return tl
