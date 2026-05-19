r"""
>>> from SingleNumberII import singleNumber
>>> singleNumber([2, 2, 3, 2])
3
>>> singleNumber([0, 1, 0, 1, 0, 1, 99])
99
"""

from typing import List


def singleNumber(nums: List[int]) -> int:
    """Finds the integer that appears once in ``nums`` where all other integers
    appear 3 times.
    """
    bits = 32 * [0]
    for num in nums:
        for i in range(32):
            bits[i] += getBit(num, i)

    bits = [bit % 3 for bit in bits]

    ans = 0
    for i in range(32):
        ans += bits[i] << i

    return ans if ans < 2**31 else ans - 2**32


def getBit(num, i):
    """Gets the ``i``-th bit of ``num``.
    """
    return (num >> i) & 1
