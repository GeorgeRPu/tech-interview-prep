r"""
>>> from find_the_duplicate_number__negation_marking import findDuplicate
>>> findDuplicate([1, 3, 4, 2, 2])
2
>>> findDuplicate([3, 1, 3, 4, 2])
3
>>> findDuplicate([3, 3, 3, 3, 3])
3
"""

from typing import List

def findDuplicate(nums: List[int]) -> int:
    for i in range(len(nums)):
        n = abs(nums[i])
        if nums[n] < 0:
            return n
        else:
            nums[n] = -nums[n]

    return -1
