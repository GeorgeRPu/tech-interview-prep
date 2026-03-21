r"""
Problem
-------
https://leetcode.com/problems/two-sum/

Given an array of integers ``nums`` and an integer ``target``, return
*indices of the two numbers such that they add up to ``target``*.

You may assume that each input would have **exactly one solution**, and
you may not use the *same* element twice.

You can return the answer in any order.

 

**Example 1:**

::


   Input: nums = [2,7,11,15], target = 9
   Output: [0,1]
   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

::


   Input: nums = [3,2,4], target = 6
   Output: [1,2]

**Example 3:**

::


   Input: nums = [3,3], target = 6
   Output: [0,1]

 

**Constraints:**

- ``2 <= nums.length <= 10``\ :sup:```4```
- ``-10``\ :sup:```9```\ ``<= nums[i] <= 10``\ :sup:```9```
- ``-10``\ :sup:```9```\ ``<= target <= 10``\ :sup:```9```
- **Only one valid answer exists.**

 

**Follow-up: **\ Can you come up with an algorithm that is less than
``O(n``\ :sup:```2```\ ``)`` time complexity?

Solution
--------
Suppose ``nums`` is sorted. Set two pointers ``i`` and ``j`` to the beginning
and end of ``nums``. If ``twosum = nums[i] + nums[j]`` is less than ``target``,
we can increase ``twosum`` by using a larger ``nums[i]`` by incrementing ``i``.
If ``twosum`` is greater than ``target``, we can decrease ``twosum`` by using a
smaller ``nums[j]`` by decrementing ``j``. Stop when ``twosum == target``. This
algorithm can find the ``twosum`` in :math:`O(n \\log n)` time and no extra
space.

Pattern
-------
Array, Hash Table

Code
----

.. literalinclude:: ../solutions/easy/TwoSum.py
    :language: python
    :lines: 87-

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
