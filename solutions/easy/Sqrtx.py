r"""
Problem
-------
https://leetcode.com/problems/sqrtx/

Given a non-negative integer ``x``, return *the square root of* ``x``
*rounded down to the nearest integer*. The returned integer should be
**non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use ``pow(x, 0.5)`` in c++ or ``x ** 0.5`` in
  python.

 

**Example 1:**

::


   Input: x = 4
   Output: 2
   Explanation: The square root of 4 is 2, so we return 2.

**Example 2:**

::


   Input: x = 8
   Output: 2
   Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

**Constraints:**

- ``0 <= x <= 2``\ :sup:```31```\ ``- 1``

Solution
--------
Finding the square root of :math:`x` is equivalent to finding :math:`y` such
that :math:`y^2 = x`. We can use binary search to find :math:`y` in the range
:math:`[0, \sqrt{2^{32} - 1}] \approx [0, 2^{16}]`. After narrowing the range
of possible square roots to within 1, within 1, we return the beginning of the
range.

Pattern
-------
Math, Binary Search

Code
----

.. literalinclude:: ../solutions/easy/Sqrtx.py
    :language: python
    :lines: 70-

Test
----
>>> from Sqrtx import mySqrt
>>> mySqrt(4)
2
>>> mySqrt(8)
2
"""


def mySqrt(x: int) -> int:
    """Finds the largest integer :math:`y` such that :math:`y^2 \\leq x`.
    """
    start = 0
    end = 65536
    while start + 1 < end:
        mid = (start + end) // 2
        if mid**2 > x:
            end = mid
        else:
            start = mid

    return start
