r"""
>>> from kth_largest_element_in_a_stream__min_heap import KthLargest
>>> kl = KthLargest(3, [4, 5, 8, 2])
>>> kl.add(3)
4
>>> kl.add(5)
5
>>> kl.add(10)
5
>>> kl.add(9)
8
>>> kl.add(4)
8
"""

import heapq


class KthLargest:
    """Tracks the kth largest element in a stream of values."""

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap: list[int] = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        """Add ``val`` and return the kth largest element."""
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
