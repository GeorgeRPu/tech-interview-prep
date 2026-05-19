r"""
>>> from two_sum__hash_map import twoSum
>>> twoSum([2, 7, 11, 15], 9)
[0, 1]
>>> twoSum([3, 2, 4], 6)
[1, 2]
>>> twoSum([3, 3], 6)
[0, 1]
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """Find two numbers in ``nums`` that add up to ``target``.
    """
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    return []
