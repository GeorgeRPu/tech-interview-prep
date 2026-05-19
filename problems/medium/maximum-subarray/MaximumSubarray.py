r"""
>>> from MaximumSubarray import maxSubArray
>>> maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
6
>>> maxSubArray([1])
1
"""

from typing import List


def maxSubArray(nums: List[int]) -> int:
    """Returns the maximum sum of a contiguous subarray of ``nums``.
    """
    s = 0
    max_sum = float('-inf')
    for num in nums:
        s += num
        if s > max_sum:
            max_sum = s
        if s < 0:
            s = 0
    return max_sum
