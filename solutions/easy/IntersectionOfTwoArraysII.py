"""
Problem
-------
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays ``nums1`` and ``nums2``, return *an array of
their intersection*. Each element in the result must appear as many
times as it shows in both arrays and you may return the result in **any
order**.

 

**Example 1:**

::


   Input: nums1 = [1,2,2,1], nums2 = [2,2]
   Output: [2,2]

**Example 2:**

::


   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
   Output: [4,9]
   Explanation: [9,4] is also accepted.

 

**Constraints:**

- ``1 <= nums1.length, nums2.length <= 1000``
- ``0 <= nums1[i], nums2[i] <= 1000``

 

**Follow up:**

- What if the given array is already sorted? How would you optimize your
  algorithm?
- What if ``nums1``'s size is small compared to ``nums2``'s size? Which
  algorithm is better?
- What if elements of ``nums2`` are stored on disk, and the memory is
  limited such that you cannot load all elements into the memory at
  once?

Solution
--------
Count the number of times each number appears in each array in 2 dictionaries
``dict1`` and ``dict2``. For each ``key`` in ``dict1`` and ``dict2``, add
``key`` repeated ::

    min(dict1[key], dict2[key])

times to the intersection
list.

Pattern
-------
Array, Hash Table, Two Pointers, Binary Search, Sorting

Code
----

.. literalinclude:: ../solutions/easy/IntersectionOfTwoArraysII.py
    :language: python
    :lines: 80-

Test
----
>>> from IntersectionOfTwoArraysII import intersect
>>> intersect([1,2,2,1], [2,2])
[2, 2]
>>> intersect([4,9,5], [9,4,9,8,4])
[4, 9]
"""

from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    dict1 = counts(nums1)
    dict2 = counts(nums2)

    intersection = []
    for key, val in dict1.items():
        if key in dict2:
            repeat = min(val, dict2[key])
            intersection.extend(repeat * [key])

    return intersection


def counts(nums):
    d = {}
    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d
