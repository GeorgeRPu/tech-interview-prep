"""
Problem
-------
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Solution
--------
Position ``i = 2`` to start from the third element of ``nums``. If the current
element ``nums[i]`` equals the element two indices before ``nums[i - 2]``, look
ahead to the next element by incrementing an offset. If the current element
``nums[i + offset]`` is unequal to ``nums[i - 2]``, then copy
``nums[i + offset]`` to ``nums[i]`` and increment ``i``. Repeat until
``i + offset`` is out of bounds.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/RemoveDuplicatesFromSortedArrayII.py

.. literalinclude:: ../solutions/RemoveDuplicatesFromSortedArrayII.py
    :language: python
    :lines: 36-

Test
----
>>> from RemoveDuplicatesFromSortedArrayII import removeDuplicates
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
