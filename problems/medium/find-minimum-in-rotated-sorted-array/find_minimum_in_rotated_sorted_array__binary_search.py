r"""
>>> from find_minimum_in_rotated_sorted_array__binary_search import findMin
>>> findMin([3, 4, 5, 1, 2])
1
>>> findMin([4, 5, 6, 7, 0, 1, 2])
0
>>> findMin([11, 13, 15, 17])
11
"""


def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
