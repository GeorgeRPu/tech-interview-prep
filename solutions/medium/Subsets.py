r"""
Problem
-------
https://leetcode.com/problems/subsets/

Given an integer array ``nums`` of **unique** elements, return *all
possible* subsets *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the
solution in **any order**.

 

**Example 1:**

::


   Input: nums = [1,2,3]
   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

**Example 2:**

::


   Input: nums = [0]
   Output: [[],[0]]

 

**Constraints:**

- ``1 <= nums.length <= 10``
- ``-10 <= nums[i] <= 10``
- All the numbers of ``nums`` are **unique**.

Solution
--------
We can generate the power set recursively. Every subset of ``nums`` either
includes ``nums[0]`` or it doesn't. If we already have the power set of
``nums[1:]``, we can extend the power set of ``nums`` by taking every subset
:math:`S` of ``nums[1:]`` both as-is and with ``nums[0]`` prepended (including
it):

.. math ::

   P(\texttt{nums}) = P(\texttt{nums[1:]}) \;\cup\; \{ \{\texttt{nums[0]}\} \cup S : S \in P(\texttt{nums[1:]})\}

The base case is the empty array, whose only subset is the empty set.

Pattern
-------
Array, Backtracking, Bit Manipulation

Code
----

.. literalinclude:: ../solutions/medium/Subsets.py
    :language: python
    :lines: 81-

Test
----
>>> from Subsets import compare_collections, subsets
>>> s = subsets([1, 2, 3])
>>> expected_s = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
>>> compare_collections(s, expected_s)
True
>>> s = subsets([0])
>>> expected_s = [[], [0]]
>>> compare_collections(s, expected_s)
True

Complexity
----------
| :math:`n` is the length of the input array
| Time: :math:`O(2^n)` — there are :math:`2^n` subsets of an :math:`n`-element set, and we need to generate each one
| Auxiliary Space: :math:`O(1)`
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Return the power set of ``nums``.
    """
    if len(nums) == 0:
        return [[]]
    else:
        element = nums[0]
        new_nums = nums[1:]
        return [subset for subset in subsets(new_nums)] \
            + [[element] + subset for subset in subsets(new_nums)]


def compare_collections(collection1: List[List[int]], collection2: List[List[int]]) -> bool:
    """Helper function to compare whether two collections (as lists of lists)
    are equal.
    """
    collection1 = {frozenset(subset) for subset in collection1}
    collection2 = {frozenset(subset) for subset in collection2}
    return collection1 == collection2
