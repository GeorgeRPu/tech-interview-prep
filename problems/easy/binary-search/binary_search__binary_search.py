r"""
>>> from binary_search__iterative import search
>>> search([-1, 0, 3, 5, 9, 12], 9)
4
>>> search([-1, 0, 3, 5, 9, 12], 2)
-1
"""


def search(nums: list[int], target: int) -> int:
    """Search for ``target`` in sorted ``nums`` using binary search."""
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
