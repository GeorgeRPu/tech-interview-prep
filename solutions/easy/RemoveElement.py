"""
Problem
-------
https://leetcode.com/problems/remove-element

Solution
--------
Start from the first element of ``nums``. If the current element ``nums[i]``
equals ``val``, look ahead to the next element by incrementing an offset. If
the current element ``nums[i + offset]`` is unequal to ``val``, then copy
``nums[i + offset]`` to ``nums[i]`` and increment ``i``. Repeat until
``i + offset`` is out of bounds.

Code
----

.. literalinclude:: ../solutions/easy/RemoveElement.py
    :language: python
    :lines: 34-

Test
----
>>> from RemoveElement import removeElement
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
