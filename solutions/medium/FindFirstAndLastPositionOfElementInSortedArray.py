"""
Problem
-------
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Solution
--------
First perform binary search to find the ``index`` of any ``target`` in the
array. Divide ``nums`` into 2 halves: left of ``index`` and right of ``index``.
If we perform binary search again on the left half, we get a new index
``right`` for a ``target`` element in ``nums`` left of ``index``. If we cannot
find ``target``, then ``index`` must be the left-most position of any ``target``
value in ``nums``. Thus we recursively perform binary search using ``left``
until we can no longer find ``target`` and use the previous ``left`` value as
the lower bound. Similarly, we recursively perform binary search on the right
half until we can no longer find target.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/FindFirstAndLastPositionOfElementInSortedArray.py

.. literalinclude:: ../solutions/medium/FindFirstAndLastPositionOfElementInSortedArray.py
    :language: python
    :lines: 37-

Test
----
>>> from FindFirstAndLastPositionOfElementInSortedArray import searchRange
>>> searchRange([5, 7, 7, 8, 8, 10], 8)
[3, 4]
>>> searchRange([5, 7, 7, 8, 8, 10], 6)
[-1, -1]
>>> searchRange([], 0)
[-1, -1]
"""

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    """Finds the first and last position of ``target`` in the sorted array
    ``nums``.
    """
    n = len(nums)
    index = binary_search(nums, target, 0, n - 1)
    left = index
    right = index

    while True:
        left_candidate = binary_search(nums, target, 0, left - 1)
        right_candidate = binary_search(nums, target, right + 1, n - 1)
        if left_candidate == -1 and right_candidate == -1:
            break
        if left_candidate != -1:
            left = left_candidate
        if right_candidate != -1:
            right = right_candidate

    return [left, right]


def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
    """Performs binary search on the sorted array ``nums`` between ``left`` and
    ``right`` to find ``target``.
    """
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1
