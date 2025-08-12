"""
Problem
-------
https://leetcode.com/problems/contains-duplicate-ii/

Solution
--------
Track the indices of each number in a dictionary. We only need to track the
most recent index for each number as, if there is a preceding index ``i1`` for
the current index ``j`` such that ``nums[i1] == nums[j]`` and
``abs(i - j) <= k``, then the most recent index ``i2`` will also satisfy the
above conditions. Iterate through ``nums``. If the current number is in the
dictionary ``d`` and the difference between the current index ``i`` and
``d[i]`` is :math:`\leq k`, return ``True``. Otherwise, update the most recent
index of the current number in ``d``. If we reach the end of ``nums``, return
``False``.

Code
----

.. literalinclude:: ../solutions/easy/ContainsDuplicateII.py
    :language: python
    :lines: 36-

Test
----
>>> from ContainsDuplicateII import containsNearbyDuplicate
>>> containsNearbyDuplicate([1, 2, 3, 1], 3)
True
>>> containsNearbyDuplicate([1, 0, 1, 1], 1)
True
>>> containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
False
"""

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """Returns whether there are two distinct indices ``i`` and ``j`` such that
    ``nums[i] == nums[j]`` and ``abs(i - j) <= k``.
    """
    d = {}
    for i, num in enumerate(nums):
        if num in d and abs(i - d[num]) <= k:
            return True
        else:
            d[num] = i

    return False
