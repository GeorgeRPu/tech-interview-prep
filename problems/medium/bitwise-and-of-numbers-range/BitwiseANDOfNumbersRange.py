r"""
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
