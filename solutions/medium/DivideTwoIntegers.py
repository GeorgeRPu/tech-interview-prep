"""
Problem
-------
https://leetcode.com/problems/divide-two-integers/

Solution
--------
We can use repeated subtraction of the dividend by the divisor to find the
quotient without using multiplication, division, or modulus. However, loops in
Python are slow so we will time out for large dividends and small divisors.
Instead use  ``len(range(0, stop, step))`` to find the quotient. Since
``range(0, stop, step)`` yields 1 element even if ``stop < step``, put
``stop = abs(dividend) - abs(divisor) + 1`` and ``stop = abs(divisor)``. Adjust
the sign of the quotient when :math:`(dividend < 0) \\oplus (divisor < 0)`.
Clamp the quotient to be in :math:`[-2^{31}, 2^{31} - 1]`.

Code
----

.. literalinclude:: ../solutions/medium/DivideTwoIntegers.py
    :language: python
    :lines: 32-

Test
----
>>> from DivideTwoIntegers import divide
>>> divide(10, 3)
3
>>> divide(7, -3)
-2
"""


def divide(dividend: int, divisor: int) -> int:
    quotient = len(range(0, abs(dividend) - abs(divisor) + 1, abs(divisor)))

    if (dividend < 0) ^ (divisor < 0):
        quotient = -quotient

    return max(min(quotient, 2**31 - 1), -2**31)
