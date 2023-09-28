"""
Problem
-------
https://leetcode.com/problems/h-index/

Solution
--------
Sort the citations in descending order. Then the h-index is the largest index
of ``citations`` such that all the citation counts to the left are at least as
large as h. We can find this index by iterating through ``citations`` and
breaking when the index becomes greater than the citation count.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/HIndex.py

.. literalinclude:: ../solutions/HIndex.py
    :language: python
    :lines: 33-

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
