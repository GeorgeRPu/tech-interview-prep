r"""
Problem
-------
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array ``nums`` sorted in ascending order (with
**distinct** values).

Prior to being passed to your function, ``nums`` is **possibly left
rotated** at an unknown index ``k`` (``1 <= k < nums.length``) such that
the resulting array is
``[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]``
(**0-indexed**). For example, ``[0,1,2,4,5,6,7]`` might be left rotated
by ``3`` indices and become ``[4,5,6,7,0,1,2]``.

Given the array ``nums`` **after** the possible rotation and an integer
``target``, return *the index of* ``target`` *if it is in* ``nums``\ *,
or* ``-1`` *if it is not in* ``nums``.

You must write an algorithm with ``O(log n)`` runtime complexity.

 

**Example 1:**

::

   Input: nums = [4,5,6,7,0,1,2], target = 0
   Output: 4

**Example 2:**

::

   Input: nums = [4,5,6,7,0,1,2], target = 3
   Output: -1

**Example 3:**

::

   Input: nums = [1], target = 0
   Output: -1

 

**Constraints:**

- ``1 <= nums.length <= 5000``
- ``-10``\ :sup:```4```\ ``<= nums[i] <= 10``\ :sup:```4```
- All values of ``nums`` are **unique**.
- ``nums`` is an ascending array that is possibly rotated.
- ``-10``\ :sup:```4```\ ``<= target <= 10``\ :sup:```4```

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

Pattern
-------
Array, Binary Search

Code
----

.. literalinclude:: ../solutions/medium/SearchInRotatedArray.py
    :language: python
    :lines: 106-

Test
----
>>> from SearchInRotatedArray import search
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
