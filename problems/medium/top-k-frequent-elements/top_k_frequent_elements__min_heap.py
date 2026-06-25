r"""
>>> from top_k_frequent_elements__min_heap import topKFrequent
>>> sorted(topKFrequent([1, 1, 1, 2, 2, 3], 2))
[1, 2]
>>> topKFrequent([1], 1)
[1]
"""

import heapq
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    """Return the ``k`` most frequent elements using bucket sort."""
    counter = Counter(nums)

    heap = []
    for num, count in counter.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]
