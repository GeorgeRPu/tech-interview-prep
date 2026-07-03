r"""
>>> from insert_interval__insert_then_merge import insert
>>> insert([[1, 3], [6, 9]], [2, 5])
[[1, 5], [6, 9]]
>>> insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
[[1, 2], [3, 10], [12, 16]]
>>> insert([], [5, 7])
[[5, 7]]
"""


def insert(
    intervals: list[list[int]], newInterval: list[int]
) -> list[list[int]]:
    """Insert *newInterval* then merge overlapping intervals."""
    if not intervals:
        return [newInterval]

    new_start, new_end = newInterval
    for i, (start, end) in enumerate(intervals):
        if start >= new_start:
            intervals.insert(i, newInterval)
            break
    else:
        intervals.append(newInterval)

    result = [intervals[0]]
    for i in range(1, len(intervals)):
        a, b = result[-1]
        c, d = intervals[i]
        if c <= b:
            result[-1] = [a, max(b, d)]
        else:
            result.append([c, d])

    return result
