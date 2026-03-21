"""
Problem
-------
https://leetcode.com/problems/h-index/

Given an array of integers ``citations`` where ``citations[i]`` is the
number of citations a researcher received for their ``i``\ :sup:```th```
paper, return *the researcher's h-index*.

According to the `definition of h-index on
Wikipedia <https://en.wikipedia.org/wiki/H-index>`__: The h-index is
defined as the maximum value of ``h`` such that the given researcher has
published at least ``h`` papers that have each been cited at least ``h``
times.

 

**Example 1:**

::


   Input: citations = [3,0,6,1,5]
   Output: 3
   Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
   Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

**Example 2:**

::


   Input: citations = [1,3,1]
   Output: 1

 

**Constraints:**

- ``n == citations.length``
- ``1 <= n <= 5000``
- ``0 <= citations[i] <= 1000``

Solution
--------
Sort the citations in descending order. Then the h-index is the largest index
of ``citations`` such that all the citation counts to the left are at least as
large as h. We can find this index by iterating through ``citations`` and
breaking when the index becomes greater than the citation count.

Pattern
-------
Array, Sorting, Counting Sort

Code
----

.. literalinclude:: ../solutions/medium/HIndex.py
    :language: python
    :lines: 71-

Test
----
>>> from HIndex import hIndex
>>> hIndex([3, 0, 6, 1, 5])
3
>>> hIndex([1, 3, 1])
1
"""

from typing import List


def hIndex(citations: List[int]) -> int:
    citations = reversed(sorted(citations))
    for h, citation_count in enumerate(citations):
        if h >= citation_count:
            return h

    return len(citations)
