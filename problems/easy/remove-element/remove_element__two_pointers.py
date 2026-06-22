r"""
>>> from remove_element__two_pointers import removeElement
>>> nums = [3, 2, 2, 3]
>>> k = removeElement(nums, 3)
>>> nums[:k]
[2, 2]
>>> nums = [0, 1, 2, 2, 3, 0, 4, 2]
>>> k = removeElement(nums, 2)
>>> nums[:k]
[0, 1, 3, 0, 4]
"""

from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """Removes all instances of ``val`` from the array ``nums`` in-place.
    """
    i = 0
    offset = 0
    while i + offset < len(nums):
        if nums[i + offset] == val:
            offset += 1
        else:
            nums[i] = nums[i + offset]
            i += 1

    return len(nums) - offset
