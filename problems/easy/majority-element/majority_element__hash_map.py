r"""
>>> from majority_element__hash_map import majorityElement
>>> majorityElement([3, 2, 3])
3
>>> majorityElement([2, 2, 1, 1, 1, 2, 2])
2
>>> majorityElement([1])
1
"""


def majorityElement(nums: list[int]) -> int:
    """Returns the element that appears more than :math:`\\lfloor n/2 \\rfloor`
    times in the list.
    """
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

        if counts[n] > len(nums) // 2:
            return n
