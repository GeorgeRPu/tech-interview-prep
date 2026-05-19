r"""
>>> from MissingNumber import missingNumber
>>> list1 = list(range(4))
>>> list1.remove(2)
>>> missingNumber(list1)
2
>>> list2 = list(range(100))
>>> list2.remove(47)
>>> missingNumber(list2)
47
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    """Find the single missing number in a list of integers.
    """
    n = len(nums)
    s = sum(nums)
    return n * (n + 1) // 2 - s
