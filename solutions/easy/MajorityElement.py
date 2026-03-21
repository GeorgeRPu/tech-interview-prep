"""
Problem
-------
https://leetcode.com/problems/majority-element/

Given an array ``nums`` of size ``n``, return *the majority element*.

The majority element is the element that appears more than ``⌊n / 2⌋``
times. You may assume that the majority element always exists in the
array.

 

**Example 1:**

::

   Input: nums = [3,2,3]
   Output: 3

**Example 2:**

::

   Input: nums = [2,2,1,1,1,2,2]
   Output: 2

 

**Constraints:**

- ``n == nums.length``
- ``1 <= n <= 5 * 10``\ :sup:```4```
- ``-10``\ :sup:```9```\ ``<= nums[i] <= 10``\ :sup:```9```
- The input is generated such that a majority element will exist in the
  array.

 

**Follow-up:** Could you solve the problem in linear time and in
``O(1)`` space?

Solution
--------
Use a dictionary to count the occurrences of each element in ``nums``. We can
break early once the count of an element exceeds :math:`\\lfloor n/2 \\rfloor`.

Pattern
-------
Array, Hash Table, Divide and Conquer, Sorting, Counting

Code
----

.. literalinclude:: ../solutions/easy/MajorityElement.py
    :language: python
    :lines: 70-

Test
----
>>> from MajorityElement import majorityElement
>>> majorityElement([3, 2, 3])
3
>>> majorityElement([2, 2, 1, 1, 1, 2, 2])
2
>>> majorityElement([1])
1
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    """Returns the element that appears more than :math:`\\lfloor n/2 \\rfloor`
    times in the list.
    """
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

        if counts[n] > len(nums) // 2:
            return n
