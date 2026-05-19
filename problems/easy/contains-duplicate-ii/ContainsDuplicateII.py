r"""
>>> from ContainsDuplicateII import containsNearbyDuplicate
>>> containsNearbyDuplicate([1, 2, 3, 1], 3)
True
>>> containsNearbyDuplicate([1, 0, 1, 1], 1)
True
>>> containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
False
"""

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """Returns whether there are two distinct indices ``i`` and ``j`` such that
    ``nums[i] == nums[j]`` and ``abs(i - j) <= k``.
    """
    d = {}
    for i, num in enumerate(nums):
        if num in d and abs(i - d[num]) <= k:
            return True
        else:
            d[num] = i

    return False
