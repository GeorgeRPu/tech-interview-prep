"""
Problem
-------
https://leetcode.com/problems/two-sum/

Solution
--------
Suppose ``nums`` is sorted. Set two pointers ``i`` and ``j`` to the beginning
and end of ``nums``. If ``twosum = nums[i] + nums[j]`` is less than ``target``,
we can increase ``twosum`` by using a larger ``nums[i]`` by incrementing ``i``.
If ``twosum`` is greater than ``target``, we can decrease ``twosum`` by using a
smaller ``nums[j]`` by decrementing ``j``. Stop when ``twosum == target``. This
algorithm can find the ``twosum`` in :math:`O(n \\log n)` time and no extra
space.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/TwoSum.py

.. literalinclude:: ../solutions/easy/TwoSum.py
    :language: python
    :lines: 35-

Test
----
>>> from TwoSum import twoSum
>>> twoSum([2,7,11,15], 9)
[0, 1]
>>> twoSum([3,2,4], 6)
[1, 2]
>>> twoSum([3, 3], 6)
[0, 1]
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """Find two numbers in ``nums`` that add up to ``target``.
    """
    nums = list(enumerate(nums))  # keep track of the orignal indices
    nums = sorted(nums, key=lambda x: x[1])
    i = 0
    j = len(nums) - 1
    while i < j:
        twosum = nums[i][1] + nums[j][1]
        if twosum == target:
            break
        if twosum < target:
            i = i + 1
        if twosum > target:
            j = j - 1
    return [nums[i][0], nums[j][0]]
