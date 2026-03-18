r"""
Problem
-------
https://leetcode.com/problems/maximum-subarray/

Given an integer array ``nums``, find the subarray with the largest sum,
and return *its sum*.

 

**Example 1:**

::


   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
   Output: 6
   Explanation: The subarray [4,-1,2,1] has the largest sum 6.

**Example 2:**

::


   Input: nums = [1]
   Output: 1
   Explanation: The subarray [1] has the largest sum 1.

**Example 3:**

::


   Input: nums = [5,4,-1,7,8]
   Output: 23
   Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

 

**Constraints:**

- ``1 <= nums.length <= 10``\ :sup:```5```
- ``-10``\ :sup:```4```\ ``<= nums[i] <= 10``\ :sup:```4```

 

**Follow up:** If you have figured out the ``O(n)`` solution, try coding
another solution using the **divide and conquer** approach, which is
more subtle.

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
    :lines: 80-

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
