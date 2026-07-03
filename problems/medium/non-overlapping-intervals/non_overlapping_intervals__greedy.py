r"""
>>> from non_overlapping_intervals__greedy import eraseOverlapIntervals
>>> eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
1
>>> eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
2
>>> eraseOverlapIntervals([[1, 2], [2, 3]])
0
"""


def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    """Return the minimum removals to make *intervals* non-overlapping."""
    if not intervals:
        return 0

    intervals.sort()
    result = 0
    prev_end = intervals[0][1]
    for i in range(1, len(intervals)):
        a, b = intervals[i]
        if a < prev_end:
            result += 1
            prev_end = min(prev_end, b)
        else:
            prev_end = b

    return result
