r"""
>>> from permutations__recursive import permutations
>>> permutations([1, 2])
[[1, 2], [2, 1]]
>>> permutations([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
>>> len(permutations([1, 2, 3, 4]))
24
"""


def permutations(nums: list[int]) -> list[list[int]]:
    """Generate all permutations of ``nums``.
    """
    if len(nums) > 0:
        return [[n] + p
                for i, n in enumerate(nums)
                for p in permutations(nums[:i] + nums[i + 1:])]
    else:
        return [[]]
