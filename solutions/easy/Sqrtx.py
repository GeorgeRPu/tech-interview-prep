__doc__ = r"""
Problem
-------
https://leetcode.com/problems/sqrtx/

Solution
--------
Finding the square root of :math:`x` is equivalent to finding :math:`y` such
that :math:`y^2 = x`. We can use binary search to find :math:`y` in the range
:math:`[0, \sqrt{2^{32} - 1}] \approx [0, 2^{16}]`. After narrowing the range
of possible square roots to within 1, within 1, we return the beginning of the
range.

Code
----

.. literalinclude:: ../solutions/easy/Sqrtx.py
    :language: python
    :lines: 27-

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
