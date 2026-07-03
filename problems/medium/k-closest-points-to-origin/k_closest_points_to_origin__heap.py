r"""
>>> from k_closest_points_to_origin__heap import kClosest
>>> kClosest([[1, 3], [-2, 2]], 1)
[[-2, 2]]
>>> sorted(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
[[-2, 4], [3, 3]]
"""

import heapq


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the *k* closest points to the origin."""
    heap = [(x**2 + y**2, x, y) for x, y in points]
    heapq.heapify(heap)
    return [[x, y] for _, x, y in heapq.nsmallest(k, heap)]
