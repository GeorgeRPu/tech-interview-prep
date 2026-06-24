r"""
>>> from last_stone_weight__max_heap import lastStoneWeight
>>> lastStoneWeight([2, 7, 4, 1, 8, 1])
1
>>> lastStoneWeight([1])
1
"""

import heapq


def lastStoneWeight(stones: list[int]) -> int:
    """Return the weight of the last remaining stone."""
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)
        if x != y:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0
