r"""
>>> from subsets_ii__backtracking import subsetsWithDup
>>> sorted([sorted(s) for s in subsetsWithDup([1, 2, 2])])
[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
>>> sorted([sorted(s) for s in subsetsWithDup([0])])
[[], [0]]
"""


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    result = []

    def backtrack(subset, i):
        result.append(subset.copy())

        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue

            backtrack(subset + [nums[j]], j + 1)

    backtrack([], 0)
    return result
