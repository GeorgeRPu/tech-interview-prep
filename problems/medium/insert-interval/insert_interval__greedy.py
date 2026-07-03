r"""
>>> from insert_interval__greedy import insert
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
    """Insert *newInterval* into sorted *intervals*, merging overlaps."""
    if not intervals:
        return [newInterval]

    c, d = newInterval
    result: list[list[int]] = []
    for i, (a, b) in enumerate(intervals):
        if d < a:
            result.append([c, d])
            return result + intervals[i:]
        elif c > b:
            result.append([a, b])
        else:
            c = min(a, c)
            d = max(b, d)

    result.append([c, d])
    return result
