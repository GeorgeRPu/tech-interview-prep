r"""
>>> from counting_bits__dp import countBits
>>> countBits(2)
[0, 1, 1]
>>> countBits(5)
[0, 1, 1, 2, 1, 2]
>>> countBits(0)
[0]
"""


def countBits(n: int) -> list[int]:
    """Return the number of 1-bits for each integer from 0 to *n*."""
    bits = [0] * (n + 1)
    for i in range(n + 1):
        bits[i] = bits[i >> 1] + (1 & i)
    return bits
