r"""
Problem
-------
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given two integers ``left`` and ``right`` that represent the range
``[left, right]``, return *the bitwise AND of all numbers in this range,
inclusive*.

 

**Example 1:**

::


   Input: left = 5, right = 7
   Output: 4

**Example 2:**

::


   Input: left = 0, right = 0
   Output: 0

**Example 3:**

::


   Input: left = 1, right = 2147483647
   Output: 0

 

**Constraints:**

- ``0 <= left <= right <= 2``\ :sup:```31```\ ``- 1``

Solution
--------
Consider 2 binary numbers :math:`left < right`. Observe that :math:`left` and
:math:`left + 1` differ only in the 1's bit. Then :math:`left \land (left + 1)`
is :math:`left` with the last bit set to 0. Similarly, :math:`left + 1` differ
in the 2's bit, so :math:`left \land (left + 1) \land (left + 2)` is
:math:`left` with the last 2 bits set to 0. The bitwise :math:`\land` of all
binary numbers in :math:`[left, right]` is the common prefix of :math:`left`
and :math:`right` with all other bits set to 0, as the subsequent bits will
vary in :math:`[left, right]`.

Code
----

.. literalinclude:: ../solutions/medium/BitwiseANDOfNumbersRange.py
    :language: python
    :lines: 72-

Test
----
>>> from BitwiseANDOfNumbersRange import rangeBitwiseAnd
>>> rangeBitwiseAnd(5, 7)
4
>>> rangeBitwiseAnd(0, 1)
0
>>> rangeBitwiseAnd(1, 2)
0
"""


def rangeBitwiseAnd(left: int, right: int) -> int:
    """Bitwise AND all numbers from ``left`` to ``right``, inclusive.
    """
    bit_and = 0
    for i in range(32, -1, -1):
        leftBit = getBit(left, i)
        if leftBit != getBit(right, i):
            return bit_and
        else:
            bit_and += leftBit << i

    return bit_and


def getBit(num, i):
    """Gets the ``i``-th bit of ``num``.
    """
    return (num >> i) & 1
