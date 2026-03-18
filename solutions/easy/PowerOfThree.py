"""
Problem
-------
https://leetcode.com/problems/power-of-three/

Given an integer ``n``, return *``true`` if it is a power of three.
Otherwise, return ``false``*.

An integer ``n`` is a power of three, if there exists an integer ``x``
such that ``n == 3``\ :sup:```x```.

 

**Example 1:**

::


   Input: n = 27
   Output: true
   Explanation: 27 = 33

**Example 2:**

::


   Input: n = 0
   Output: false
   Explanation: There is no x where 3x = 0.

**Example 3:**

::


   Input: n = -1
   Output: false
   Explanation: There is no x where 3x = (-1).

 

**Constraints:**

- ``-2``\ :sup:```31```\ ``<= n <= 2``\ :sup:```31```\ ``- 1``

 

**Follow up:** Could you solve it without loops/recursion?

Solution
--------
Note that, if :math:`n = 3^x`, :math:`n` can never be negative. For positive
:math:`n``, check if :math:`n` is divisble by 3. If it is, divide :math:`n` by
3 and check again. If it is not, then :math:`n` is not a power of 3.

Code
----

.. literalinclude:: ../solutions/easy/PowerOfThree.py
    :language: python
    :lines: 76-

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
