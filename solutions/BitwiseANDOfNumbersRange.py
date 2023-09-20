r"""
Problem
-------
https://leetcode.com/problems/bitwise-and-of-numbers-range/

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
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/SetMatrixZeroes.py

.. literalinclude:: ../solutions/BitwiseANDOfNumbersRange.py
    :language: python
    :lines: 37-

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
