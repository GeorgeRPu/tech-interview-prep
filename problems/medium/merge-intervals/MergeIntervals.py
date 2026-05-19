r"""
>>> from MergeIntervals import merge
>>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
[[1, 6], [8, 10], [15, 18]]
>>> merge([[1, 4], [4, 5]])
[[1, 5]]
"""

from __future__ import annotations

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
