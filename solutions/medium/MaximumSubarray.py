r"""
Problem
-------
https://leetcode.com/problems/maximum-subarray/

Solution
--------
Observe that the maximum sum of a contiguous subarray of ``nums`` ending at
index ``i`` is

.. math::
    s_i = \max(s_{i-1} + \mathtt{nums[i]}, \mathtt{nums[i]}).


The only time we reset the sum is when :math:`s_{i-1} < 0`. Iterate through
``nums``, summing each element and updating the maximum sum as we go. If the
sum dips below 0, reset it to 0.

Code
----

.. literalinclude:: ../solutions/medium/MaximumSubarray.py
    :language: python
    :lines: 29-

Test
----
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
