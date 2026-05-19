r"""
>>> from summary_ranges__approach_1 import summaryRanges
>>> summaryRanges([0, 1, 2, 4, 5, 7])
['0->2', '4->5', '7']
>>> summaryRanges([0, 2, 3, 4, 6, 8, 9])
['0', '2->4', '6', '8->9']
"""

from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    """Return the smallest sorted list of ranges that cover all the numbers in
    ``nums``.
    """
    summary_ranges = []

    i = 0
    while i < len(nums):
        start = nums[i]

        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1

        summary_ranges.append(get_range_str(start, nums[i]))
        i += 1

    return summary_ranges


def get_range_str(start, end):
    """Get the range from ``start`` to ``end`` as a formatted string.
    """
    return str(start) if start == end else f'{start}->{end}'
