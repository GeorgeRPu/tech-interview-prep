r"""
>>> from number_of_1_bits__bit_scan import hammingWeight
>>> hammingWeight(11)
3
>>> hammingWeight(128)
1
>>> hammingWeight(2147483645)
30
"""


def hammingWeight(n: int) -> int:
    """Return the number of set bits in *n*."""
    result = 0
    for i in range(32):
        if (1 << i) & n:
            result += 1
    return result
