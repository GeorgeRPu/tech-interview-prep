r"""
>>> from jump_game__approach_1 import canJump
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
