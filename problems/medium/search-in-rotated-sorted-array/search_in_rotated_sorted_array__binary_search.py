r"""
>>> from search_in_rotated_sorted_array__binary_search import search
>>> search([4, 5, 6, 7, 0, 1, 2], 0)
4
>>> search([4, 5, 6, 7, 0, 1, 2], 3)
-1
>>> search([1], 0)
-1
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """Searches for ``target`` in sorted array ``nums`` rotated by a pivot.
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[0]:
            if nums[mid] < target:
                left = mid + 1
            elif nums[left] > target:
                left = mid + 1
            else:
                right = mid - 1

        else:
            if nums[mid] > target:
                right = mid - 1
            elif nums[right] < target:
                right = mid - 1
            else:
                left = mid + 1

    return -1
