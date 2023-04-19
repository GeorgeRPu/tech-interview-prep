from __future__ import annotations

__doc__ = """
Problem
-------
https://leetcode.com/problems/merge-intervals/

Solution
--------
The key step is to sort ``intervals`` by their start point. We start merging
intervals from left to right. Add the first interval to ``merged_intervals``.
Suppose we have 2 sorted intervals :math:`[a, b]` in ``merged_intervals`` and
and :math:`[c, d]` in ``intervals``. We only need to check that :math:`c > b`
to merge the intervals to obtain :math:`[a, \\max(b, d)]`. Moreover, we only need to check
the next interval in ``intervals`` against the rightmost merged interval. This
is because the merged intervals are all disjoint and sorted from left to right.

Code
----
https://github.com/GeorgeRPu/tech-interview-prep/blob/main/solutions/MergeIntervals.py

.. literalinclude:: ../solutions/MergeIntervals.py
    :language: python
    :lines: 35-

Test
----
>>> from MergeIntervals import merge
>>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
[[1, 6], [8, 10], [15, 18]]
>>> merge([[1, 4], [4, 5]])
[[1, 5]]
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals.
    """
    intervals = sorted(intervals, key=lambda interval: interval[0])
    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        [a, b] = merged_intervals[-1]
        [c, d] = interval

        if c <= b:
            merged_intervals[-1][1] = max(b, d)
        else:
            merged_intervals.append(interval)

    return merged_intervals
