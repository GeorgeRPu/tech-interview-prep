r"""
>>> from sum_of_two_integers__bit_manipulation import getSum
>>> getSum(1, 2)
3
>>> getSum(2, 3)
5
>>> getSum(-1, 1)
0
"""


def getSum(a: int, b: int) -> int:
    """Return the sum of *a* and *b* without ``+`` or ``-``."""
    result = 0
    carry = 0

    for i in range(32):
        bit_a = (1 << i) & a
        bit_b = (1 << i) & b

        s = bit_a ^ bit_b ^ carry
        carry = ((bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)) << 1

        result |= (1 << i) & s

    if result & 0x80000000:
        return ~(result ^ 0xFFFFFFFF)
    return result
