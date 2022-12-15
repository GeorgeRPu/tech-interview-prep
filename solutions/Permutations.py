"""
Problem
-------
https://leetcode.com/problems/permutations/

Solution
--------
We can generate permutations inductively. Suppose we have all the permutations
of ``nums[1:]``. If we prepend ``nums[1]`` to these permutations, we now have
all permutations of ``nums`` that start with ``nums[1]``. Doing this for each
:math:`n` in ``nums``, we can generate every permutation of ``nums``.

Code
----
https://github.com/GeorgeRPu/Tech-Interview-Prep/blob/main/solutions/Permutations.py

.. literalinclude:: ../solutions/Permutations.py
    :language: python
    :lines: 32-

Test
----
>>> from Permutations import permutations
>>> permutations([1, 2])
[[1, 2], [2, 1]]
>>> permutations([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
>>> len(permutations([1, 2, 3, 4]))
24
"""

from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    """Generate all permutations of ``nums``.
    """
    if len(nums) > 0:
        return [[n] + p
                for i, n in enumerate(nums)
                for p in permutations(nums[:i] + nums[i + 1:])]
    else:
        return [[]]
