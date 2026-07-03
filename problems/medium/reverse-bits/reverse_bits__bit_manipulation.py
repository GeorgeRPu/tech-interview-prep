r"""
>>> from reverse_bits__bit_manipulation import reverseBits
>>> reverseBits(43261596)
964176192
>>> reverseBits(4294967293)
3221225471
"""


def reverseBits(n: int) -> int:
    """Reverse the bits of a 32-bit unsigned integer."""
    result = 0
    for i in range(32):
        if (1 << i) & n:
            result |= 1 << (31 - i)
    return result
