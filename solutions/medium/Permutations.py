"""
Problem
-------
https://leetcode.com/problems/permutations/

Given an array ``nums`` of distinct integers, return all the possible
permutations. You can return the answer in **any order**.

 

**Example 1:**

::

   Input: nums = [1,2,3]
   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

**Example 2:**

::

   Input: nums = [0,1]
   Output: [[0,1],[1,0]]

**Example 3:**

::

   Input: nums = [1]
   Output: [[1]]

 

**Constraints:**

- ``1 <= nums.length <= 6``
- ``-10 <= nums[i] <= 10``
- All the integers of ``nums`` are **unique**.

Solution
--------
We can generate permutations inductively. Suppose we have all the permutations
of ``nums[1:]``. If we prepend ``nums[1]`` to these permutations, we now have
all permutations of ``nums`` that start with ``nums[1]``. Doing this for each
:math:`n` in ``nums``, we can generate every permutation of ``nums``.

Pattern
-------
Array, Backtracking

Code
----

.. literalinclude:: ../solutions/medium/Permutations.py
    :language: python
    :lines: 69-

Test
----
>>> from Permutations import permutations
>>> permutations([1, 2])
[[1, 2], [2, 1]]
>>> permutations([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
>>> len(permutations([1, 2, 3, 4]))
24
"""

from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    """Generate all permutations of ``nums``.
    """
    if len(nums) > 0:
        return [[n] + p
                for i, n in enumerate(nums)
                for p in permutations(nums[:i] + nums[i + 1:])]
    else:
        return [[]]
