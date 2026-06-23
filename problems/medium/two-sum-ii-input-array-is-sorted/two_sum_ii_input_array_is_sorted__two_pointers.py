r"""
>>> from two_sum_ii_input_array_is_sorted__two_pointers import twoSum
>>> twoSum([2, 7, 11, 15], 9)
[1, 2]
>>> twoSum([2, 3, 4], 6)
[1, 3]
>>> twoSum([-1, 0], -1)
[1, 2]
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
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
