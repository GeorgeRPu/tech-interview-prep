r"""
>>> from remove_duplicates_from_sorted_array_ii__two_pointers import removeDuplicates
>>> nums = [1, 1, 1, 2, 2, 3]
>>> k = removeDuplicates(nums)
>>> nums[:k]
[1, 1, 2, 2, 3]
>>> nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
>>> k = removeDuplicates(nums)
>>> nums[:k]
[0, 0, 1, 1, 2, 3, 3]
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """Removes duplicates from the sorted array ``nums`` in-place such that
    each element appears at most twice.
    """
    offset = 0
    i = 2
    while i + offset < len(nums):
        if nums[i + offset] == nums[i - 2]:
            offset += 1
        else:
            nums[i] = nums[i + offset]
            i += 1

    return len(nums) - offset
