"""
Problem
-------
https://leetcode.com/problems/3sum/

Solution
--------
Sort ``nums``. We can apply the 2Sum solution by iterating ``i`` from 0 to
``len(nums) - 1`` through ``nums`` and finding any remaining 2 numbers
``nums[j], nums[k]`` such that all 3 sum to 0. Track the solutions in a set to
avoid duplicates. Moreover, if ``nums[i]`` is a repeat, we can continue to the
next iteration.

Code
----

.. literalinclude:: ../solutions/medium/ThreeSum.py
    :language: python
    :lines: 30-

Test
----
>>> from ThreeSum import threeSum
>>> threeSum([-1, 0, 1, 2, -1, -4])
[[-1, 0, 1], [-1, -1, 2]]
>>> threeSum([0, 1, 1])
[]
>>> threeSum([0, 0, 0])
[[0, 0, 0]]
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """Returns a list of triplets in ``nums`` with distinct indices that sum to
    0.
    """
    solutions = set()
    nums = sorted(nums)
    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                solutions.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
    return [list(solution) for solution in solutions]
