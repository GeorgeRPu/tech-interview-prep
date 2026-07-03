r"""
>>> from kth_largest_element_in_an_array__min_heap import findKthLargest
>>> findKthLargest([3, 2, 1, 5, 6, 4], 2)
5
>>> findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
4
"""

import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    """Return the *k*-th largest element in *nums*."""
    heap: list[int] = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
