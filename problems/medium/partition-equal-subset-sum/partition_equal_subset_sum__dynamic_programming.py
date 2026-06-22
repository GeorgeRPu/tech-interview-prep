r"""
>>> from partition_equal_subset_sum__dynamic_programming import canPartition
>>> canPartition([1, 5, 11, 5])
True
>>> canPartition([1, 2, 3, 5])
False
"""

from typing import List

def canPartition(nums: List[int]) -> bool:
    S = sum(nums)
    if S % 2 != 0:
        return False

    target = S // 2

    sums_so_far = set([0])
    for num in nums:
        next_sums_so_far = set()
        for s in sums_so_far:
            if num + s == target:
                return True
            if num + s < target:
                next_sums_so_far.add(s + num)

            next_sums_so_far.add(s)

        sums_so_far = next_sums_so_far

    return False
