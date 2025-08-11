r"""
Problem
-------
https://leetcode.com/problems/subsets/

Solution
--------
Suppose ``nums = [1, 2, ..., n]``. We can imagine each subset :math:`S` of
``nums`` as a bit vector of length ``n``, where the value at position ``i`` is
1 if :math:`i \in S` and 0 if :math:`i \notin S`. Then the power set of ``nums``
is the set of all possible bit vectors of length ``n``. Given the bit vectors
:math:`b` for the power set of ``nums[1:]``, we can generate the bit vectors
for the power set of ``nums`` by adding a 0 or 1 to the front of each bit
vector :math:`b`. The power set of ``nums`` is equal to

.. math ::

   \{ \{1\} \cup S : S \in P(\texttt{nums[1:]})\} \cup P(\texttt{nums[1:]})

Code
----

.. literalinclude:: ../solutions/medium/Subsets.py
    :language: python
    :lines: 38-

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
