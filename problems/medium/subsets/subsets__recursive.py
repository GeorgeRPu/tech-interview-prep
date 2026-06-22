r"""
>>> from subsets__recursive import compare_collections, subsets
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
