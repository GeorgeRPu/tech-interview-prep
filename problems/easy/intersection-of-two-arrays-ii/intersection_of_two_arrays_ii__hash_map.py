r"""
>>> from intersection_of_two_arrays_ii__hash_map import intersect
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
