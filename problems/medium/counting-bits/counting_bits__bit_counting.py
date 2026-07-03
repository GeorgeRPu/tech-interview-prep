r"""
>>> from counting_bits__bit_counting import countBits
>>> countBits(2)
[0, 1, 1]
>>> countBits(5)
[0, 1, 1, 2, 1, 2]
>>> countBits(0)
[0]
"""


def countBits(n: int) -> list[int]:
    """Return the number of 1-bits for each integer from 0 to *n*."""
    result = []
    for i in range(n + 1):
        bits = 0
        num = i
        while num > 0:
            num = num & (num - 1)
            bits += 1
        result.append(bits)
    return result
