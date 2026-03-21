r"""
Problem
-------
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a **1-indexed** array of integers ``numbers`` that is already
**sorted in non-decreasing order**, find two numbers such that they add
up to a specific ``target`` number. Let these two numbers be
``numbers[index``\ :sub:```1```\ ``]`` and
``numbers[index``\ :sub:```2```\ ``]`` where
``1 <= index``\ :sub:```1```\ ``< index``\ :sub:```2```\ ``<= numbers.length``.

Return *the indices of the two numbers *\ ``index``\ :sub:```1``` *and*
``index``\ :sub:```2```\ *,* **each incremented by one,** *as an integer
array* ``[index``\ :sub:```1```\ ``, index``\ :sub:```2```\ ``]`` *of
length 2.*

The tests are generated such that there is **exactly one solution**. You
**may not** use the same element twice.

Your solution must use only constant extra space.

 

**Example 1:**

::


   Input: numbers = [2,7,11,15], target = 9
   Output: [1,2]
   Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

**Example 2:**

::


   Input: numbers = [2,3,4], target = 6
   Output: [1,3]
   Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

**Example 3:**

::


   Input: numbers = [-1,0], target = -1
   Output: [1,2]
   Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

 

**Constraints:**

- ``2 <= numbers.length <= 3 * 10``\ :sup:```4```
- ``-1000 <= numbers[i] <= 1000``
- ``numbers`` is sorted in **non-decreasing order**.
- ``-1000 <= target <= 1000``
- The tests are generated such that there is **exactly one solution**.

Solution
--------
Set two pointers ``i`` and ``j`` to the beginning and end of ``numbers``. If
``twosum = numbers[i] + numbers[j]`` is less than ``target``, we can increase
``twosum`` by using a larger ``numbers[i]`` by incrementing ``i``. If ``twosum``
is greater than ``target``, we can decrease ``twosum`` by using a smaller
``numbers[j]`` by decrementing ``j``. Stop when ``twosum == target``. This
algorithm can find the ``twosum`` in :math:`O(n \\log n)` time and no extra
space.

Pattern
-------
Array, Two Pointers, Binary Search

Code
----

.. literalinclude:: ../solutions/medium/TwoSumII.py
    :language: python
    :lines: 94-

Test
----
>>> from TwoSumII import twoSum
>>> twoSum([2, 7, 11, 15], 9)
[1, 2]
>>> twoSum([2, 3, 4], 6)
[1, 3]
>>> twoSum([-1, 0], -1)
[1, 2]
"""

from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    """Find two numbers in ``numbers`` that add up to ``target`` and return
    their one offset indicies.
    """
    i = 0
    j = len(numbers) - 1
    while i < j:
        twosum = numbers[i] + numbers[j]
        if twosum == target:
            break
        elif twosum < target:
            i += 1
        else:
            j -= 1
    return [i + 1, j + 1]
