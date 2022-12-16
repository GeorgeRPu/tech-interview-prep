"""
Problem
-------
https://leetcode.com/problems/merge-sorted-array/

Solution
--------
To merge 2 sorted lists, pick the least element from the 2 lists and add
it to the result. Repeat until both of the input lists are empty. However, here
the result list is ``nums1``. Naively merging the lists into ``nums1`` would
overwrite entries in ``nums1`` that we still need to compare. To get around this,
shift the entries in ``nums1`` to the end of the list, and then merge the lists.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/MergeSortedArray.py

.. literalinclude:: ../solutions/MergeSortedArray.py
    :language: python
    :lines: 43-

Test
----
>>> from MergeSortedArray import merge
>>> nums1 = [1, 2, 3, 0, 0, 0]
>>> nums2 = [2, 5, 6]
>>> merge(nums1, 3, nums2, 3)
>>> nums1
[1, 2, 2, 3, 5, 6]
>>> nums1 = [1]
>>> nums2 = []
>>> merge(nums1, 1, nums2, 0)
>>> nums1
[1]
>>> nums1 = [0]
>>> nums2 = [1]
>>> merge(nums1, 0, nums2, 1)
>>> nums1
[1]
"""


from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    """Merge the n-length array ``nums2`` into the (m + n)-length array
    ``nums1``.
    """
    # shift all the elements of nums1 to be flush with the end of the list
    for i in range(m + n - 1, n - 1, -1):
        nums1[i] = nums1[i - n]
    for i in range(n):
        nums1[i] = 0

    # merge the two lists
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i + n] < nums2[j]:
            nums1[i + j] = nums1[i + n]
            i += 1
        else:
            nums1[i + j] = nums2[j]
            j += 1

    while i < m:
        nums1[i + j] = nums1[i + n]
        i += 1

    while j < n:
        nums1[i + j] = nums2[j]
        j += 1
