"""
Problem
-------
https://leetcode.com/problems/jump-game/

Solution
--------
The idea is to keep track of the furthest index that can be reached. If the
furthest reachable index is less than the current index, then we cannot jump
past the current index. At the end, if the furthest reachable index is equal to
the last index, then we can reach the last index. At each step, update the
furthest reachable index with the jump distance plus the current index if it is
greater than the current furthest reachable index.

Code
----

.. literalinclude:: ../solutions/medium/JumpGame.py
    :language: python
    :lines: 31-

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
