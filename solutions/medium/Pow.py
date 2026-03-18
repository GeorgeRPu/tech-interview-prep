"""
Problem
-------
https://leetcode.com/problems/powx-n/

Implement `pow(x,
n) <http://www.cplusplus.com/reference/valarray/pow/>`__, which
calculates ``x`` raised to the power ``n`` (i.e., ``x``\ :sup:```n```).

 

**Example 1:**

::


   Input: x = 2.00000, n = 10
   Output: 1024.00000

**Example 2:**

::


   Input: x = 2.10000, n = 3
   Output: 9.26100

**Example 3:**

::


   Input: x = 2.00000, n = -2
   Output: 0.25000
   Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

**Constraints:**

- ``-100.0 < x < 100.0``
- ``-2``\ :sup:```31```\ ``<= n <= 2``\ :sup:```31```\ ``-1``
- ``n`` is an integer.
- Either ``x`` is not zero or ``n > 0``.
- ``-10``\ :sup:```4```\ ``<= x``\ :sup:```n```\ ``<= 10``\ :sup:```4```

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
    :lines: 83-

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
