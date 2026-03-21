"""
Problem
-------
https://leetcode.com/problems/jump-game/

You are given an integer array ``nums``. You are initially positioned at
the array's **first index**, and each element in the array represents
your maximum jump length at that position.

Return ``true`` *if you can reach the last index, or* ``false``
*otherwise*.

 

**Example 1:**

::


   Input: nums = [2,3,1,1,4]
   Output: true
   Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**

::


   Input: nums = [3,2,1,0,4]
   Output: false
   Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

**Constraints:**

- ``1 <= nums.length <= 10``\ :sup:```4```
- ``0 <= nums[i] <= 10``\ :sup:```5```

Solution
--------
The idea is to keep track of the furthest index that can be reached. If the
furthest reachable index is less than the current index, then we cannot jump
past the current index. At the end, if the furthest reachable index is equal to
the last index, then we can reach the last index. At each step, update the
furthest reachable index with the jump distance plus the current index if it is
greater than the current furthest reachable index.

Pattern
-------
Array, Dynamic Programming, Greedy

Code
----

.. literalinclude:: ../solutions/medium/JumpGame.py
    :language: python
    :lines: 69-

Test
----
>>> from JumpGame import canJump
>>> canJump([2, 3, 1, 1, 4])
True
>>> canJump([3, 2, 1, 0, 4])
False
"""

from typing import List


def canJump(nums: List[int]) -> bool:
    """Whether it is possible to reach the last index given a list of jumps.
    """
    reachable = 0
    for i, num in enumerate(nums):
        if i <= reachable:
            reachable = max(reachable, i + num)
        else:
            return False

    return True
