r"""
>>> from sliding_window_maximum__monotonic_deque import maxSlidingWindow
>>> maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
[3, 3, 5, 5, 6, 7]
>>> maxSlidingWindow([1], 1)
[1]
"""

from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    q = deque()


    left = 0
    right = 0
    while right < len(nums):
        while len(q) > 0 and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)

        if left > q[0]:
            q.popleft()

        if (right + 1) >= k:
            output.append(nums[q[0]])
            left += 1

        right += 1

    return output
