"""
Problem
-------
https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays ``nums1`` and ``nums2``, sorted in
**non-decreasing order**, and two integers ``m`` and ``n``, representing
the number of elements in ``nums1`` and ``nums2`` respectively.

**Merge** ``nums1`` and ``nums2`` into a single array sorted in
**non-decreasing order**.

The final sorted array should not be returned by the function, but
instead be *stored inside the array* ``nums1``. To accommodate this,
``nums1`` has a length of ``m + n``, where the first ``m`` elements
denote the elements that should be merged, and the last ``n`` elements
are set to ``0`` and should be ignored. ``nums2`` has a length of ``n``.

 

**Example 1:**

::


   Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
   Output: [1,2,2,3,5,6]
   Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
   The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

**Example 2:**

::


   Input: nums1 = [1], m = 1, nums2 = [], n = 0
   Output: [1]
   Explanation: The arrays we are merging are [1] and [].
   The result of the merge is [1].

**Example 3:**

::


   Input: nums1 = [0], m = 0, nums2 = [1], n = 1
   Output: [1]
   Explanation: The arrays we are merging are [] and [1].
   The result of the merge is [1].
   Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

**Constraints:**

- ``nums1.length == m + n``
- ``nums2.length == n``
- ``0 <= m, n <= 200``
- ``1 <= m + n <= 200``
- ``-10``\ :sup:```9```\ ``<= nums1[i], nums2[j] <= 10``\ :sup:```9```

 

**Follow up:** Can you come up with an algorithm that runs in
``O(m + n)`` time?

Solution
--------
To merge 2 sorted lists, pick the least element from the 2 lists and add
it to the result. Repeat until both of the input lists are empty. However, here
the result list is ``nums1``. Naively merging the lists into ``nums1`` would
overwrite entries in ``nums1`` that we still need to compare. To get around this,
shift the entries in ``nums1`` to the end of the list, and then merge the lists.

Pattern
-------
Array, Two Pointers, Sorting

Code
----

.. literalinclude:: ../solutions/easy/MergeSortedArray.py
    :language: python
    :lines: 106-

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
