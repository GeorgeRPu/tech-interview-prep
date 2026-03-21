"""
Problem
-------
https://leetcode.com/problems/divide-two-integers/

Given two integers ``dividend`` and ``divisor``, divide two integers
**without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example, ``8.345`` would be truncated to ``8``, and
``-2.7335`` would be truncated to ``-2``.

Return *the* **quotient** *after dividing* ``dividend`` *by*
``divisor``.

**Note:** Assume we are dealing with an environment that could only
store integers within the **32-bit** signed integer range:
``[−2``\ :sup:```31```\ ``, 2``\ :sup:```31```\ ``− 1]``. For this
problem, if the quotient is **strictly greater than**
``2``\ :sup:```31```\ ``- 1``, then return
``2``\ :sup:```31```\ ``- 1``, and if the quotient is **strictly less
than** ``-2``\ :sup:```31```, then return ``-2``\ :sup:```31```.

 

**Example 1:**

::


   Input: dividend = 10, divisor = 3
   Output: 3
   Explanation: 10/3 = 3.33333.. which is truncated to 3.

**Example 2:**

::


   Input: dividend = 7, divisor = -3
   Output: -2
   Explanation: 7/-3 = -2.33333.. which is truncated to -2.

 

**Constraints:**

- ``-2``\ :sup:```31```\ ``<= dividend, divisor <= 2``\ :sup:```31```\ ``- 1``
- ``divisor != 0``

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

Pattern
-------
Math, Bit Manipulation

Code
----

.. literalinclude:: ../solutions/medium/DivideTwoIntegers.py
    :language: python
    :lines: 83-

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
