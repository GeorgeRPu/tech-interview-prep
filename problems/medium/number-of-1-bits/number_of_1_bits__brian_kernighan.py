r"""
>>> from number_of_1_bits__brian_kernighan import hammingWeight
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
    while n > 0:
        n &= n - 1
        result += 1
    return result
