r"""
>>> from single_number__xor import singleNumber
>>> singleNumber([2, 2, 1])
1
>>> singleNumber([4, 1, 2, 1, 2])
4
>>> singleNumber([1])
1
"""


def singleNumber(nums: list[int]) -> int:
    """Return the element that appears only once."""
    result = 0
    for num in nums:
        result ^= num
    return result
