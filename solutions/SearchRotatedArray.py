"""
Problem
-------
https://leetcode.com/problems/search-in-rotated-sorted-array/

Solution
--------
https://www.youtube.com/watch?v=U8XENwh8Oy8

The array is divided into 2 parts: left of the pivot :math:`L` and right of
the pivot :math:`R`. Every element in :math:`L` is greater than every element
in :math:`R`. We can determine which part a midpoint ``mid`` is in by comparing
``nums[mid] >= nums[0]``.

Initialize ``left`` and ``right`` to the start and end of the array.

* If ``mid`` is in the left part...

  * If ``nums[mid] > target``, then ``target`` must be right of ``mid``.

  * If ``nums[mid] < target``, then ``target`` could be left of ``mid`` or
    in :math:`R` if ``target`` is small enough. We can determine which by
    comparing ``nums[left] > target``.

* If ``mid`` is in the right part...

  * If ``nums[mid] < target``, then ``target`` must be left of ``mid``.

  * If ``nums[mid] > target and nums[right] < target``, then ``target`` must be
    left of ``mid`` in :math:`L`.

  * If ``nums[mid] > target and nums[right] > target``, then ``target`` must be
    in :math:`R`.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/SearchRotatedArray.py

.. literalinclude:: ../solutions/SearchRotatedArray.py
    :language: python
    :lines: 54-

Test
----
>>> from SearchRotatedArray import search
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
