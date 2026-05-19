r"""
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
