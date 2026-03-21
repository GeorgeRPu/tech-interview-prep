r"""
Problem
-------
https://leetcode.com/problems/summary-ranges/

You are given a **sorted unique** integer array ``nums``.

A **range** ``[a,b]`` is the set of all integers from ``a`` to ``b``
(inclusive).

Return *the* **smallest sorted** *list of ranges that* **cover all the
numbers in the array exactly**. That is, each element of ``nums`` is
covered by exactly one of the ranges, and there is no integer ``x`` such
that ``x`` is in one of the ranges but not in ``nums``.

Each range ``[a,b]`` in the list should be output as:

- ``"a->b"`` if ``a != b``
- ``"a"`` if ``a == b``

 

**Example 1:**

::


   Input: nums = [0,1,2,4,5,7]
   Output: ["0->2","4->5","7"]
   Explanation: The ranges are:
   [0,2] --> "0->2"
   [4,5] --> "4->5"
   [7,7] --> "7"

**Example 2:**

::


   Input: nums = [0,2,3,4,6,8,9]
   Output: ["0","2->4","6","8->9"]
   Explanation: The ranges are:
   [0,0] --> "0"
   [2,4] --> "2->4"
   [6,6] --> "6"
   [8,9] --> "8->9"

 

**Constraints:**

- ``0 <= nums.length <= 20``
- ``-2``\ :sup:```31```\ ``<= nums[i] <= 2``\ :sup:```31```\ ``- 1``
- All the values of ``nums`` are **unique**.
- ``nums`` is sorted in ascending order.

Solution
--------
Note that subarray of consecutive numbers is a range. Iterate through the array
and keep track of the start of the range. Keep iterating as long as the next
element is consecutive. When the next element is not consecutive, create the
range string based on whether the start equals the end.

Pattern
-------
Array

Code
----

.. literalinclude:: ../solutions/easy/SummaryRanges.py
    :language: python
    :lines: 84-

Test
----
>>> from SummaryRanges import summaryRanges
>>> summaryRanges([0, 1, 2, 4, 5, 7])
['0->2', '4->5', '7']
>>> summaryRanges([0, 2, 3, 4, 6, 8, 9])
['0', '2->4', '6', '8->9']
"""

from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    """Return the smallest sorted list of ranges that cover all the numbers in
    ``nums``.
    """
    summary_ranges = []

    i = 0
    while i < len(nums):
        start = nums[i]

        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1

        summary_ranges.append(get_range_str(start, nums[i]))
        i += 1

    return summary_ranges


def get_range_str(start, end):
    """Get the range from ``start`` to ``end`` as a formatted string.
    """
    return str(start) if start == end else f'{start}->{end}'
