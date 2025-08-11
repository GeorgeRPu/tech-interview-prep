"""
Problem
-------
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Solution
--------
Set two pointers ``i`` and ``j`` to the beginning and end of ``numbers``. If
``twosum = numbers[i] + numbers[j]`` is less than ``target``, we can increase
``twosum`` by using a larger ``numbers[i]`` by incrementing ``i``. If ``twosum``
is greater than ``target``, we can decrease ``twosum`` by using a smaller
``numbers[j]`` by decrementing ``j``. Stop when ``twosum == target``. This
algorithm can find the ``twosum`` in :math:`O(n \\log n)` time and no extra
space.

Code
----

.. literalinclude:: ../solutions/medium/TwoSumII.py
    :language: python
    :lines: 32-

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
