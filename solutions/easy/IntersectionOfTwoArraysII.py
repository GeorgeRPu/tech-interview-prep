"""
Problem
-------
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Solution
--------
Count the number of times each number appears in each array in 2 dictionaries
``dict1`` and ``dict2``. For each ``key`` in ``dict1`` and ``dict2``, add
``key`` repeated ::

    min(dict1[key], dict2[key])

times to the intersection
list.

Code
----

.. literalinclude:: ../solutions/easy/IntersectionOfTwoArraysII.py
    :language: python
    :lines: 33-

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
