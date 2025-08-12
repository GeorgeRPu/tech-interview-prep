"""
Problem
-------
https://leetcode.com/problems/powx-n/

Solution
--------
We assume that using Python's built in exponentiation operator is not allowed.

.. math::

    x^n = (x^{n/2})^2 = (x^2)^{n/2}

From the first equality, we see that we can compute :math:`x^n` from
:math:`x^{n/2}` in only 1 multiplication. From the second equality, we have a
recursive formula for :math:`x^n`.::

    pow(x, n) = pow(x * x, n/2)

Adjust for the case where :math:`n` is odd and for the case where :math:`n` is
negative.

Code
----

.. literalinclude:: ../solutions/medium/Pow.py
    :language: python
    :lines: 42-

Test
----
>>> from Pow import myPow
>>> myPow(2.0, 10)
1024.0
>>> myPow(2.1, 3)
9.261000000000001
>>> myPow(2.0, -2)
0.25
"""


def myPow(x: float, n: int):
    """Raise :math:`x` to the power :math:`n`."""
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 0:
        return myPow(x * x, n // 2)
    elif n > 0:
        return myPow(x * x, n // 2) * x
    else:
        return 1 / myPow(x, -n)
