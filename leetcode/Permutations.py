"""
Problem
-------
https://leetcode.com/problems/permutations/

Solution
--------
We can generate permutations inductively. Suppose we have all the permutations
of nums[1:]. If we prepend nums[1] to these permutations, we now have all
permutations of nums that start with nums[1]. Doing this for each n in nums,
we can generate every permutation of nums.
"""

from pprint import pprint
from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    if len(nums) > 0:
        return [[n] + p
                for i, n in enumerate(nums)
                for p in permutations(nums[:i] + nums[i + 1:])]
    else:
        return [[]]


pprint(permutations([1, 2]))
pprint(permutations([1, 2, 3]))
pprint(permutations([1, 2, 3, 4]))
