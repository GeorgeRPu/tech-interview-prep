"""
Problem
-------
https://leetcode.com/problems/missing-number/

Solution
--------
Let m ∈ {1, ..., n} be the missing number. Since nums = {1, ..., n} - {m}$,

sum(nums) = ( ∑_{i=1}^{n} i ) - m
m = ∑_{i=1}^{n} i - sum(nums)

Use the formula ∑_{i=1}^{n} i = (n + 1)n/2. Note that n is one more than the
number of elements in nums.
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    s = sum(nums)
    return n * (n + 1) // 2 - s


list1 = list(range(4))
list1.remove(2)
print(missing_number(list1))
list2 = list(range(100))
list2.remove(47)
print(missing_number(list2))
