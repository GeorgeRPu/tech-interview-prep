r"""
>>> from combination_sum__backtracking import combinationSum
>>> sorted([sorted(c) for c in combinationSum([2, 3, 6, 7], 7)])
[[2, 2, 3], [7]]
>>> sorted([sorted(c) for c in combinationSum([2, 3, 5], 8)])
[[2, 2, 2, 2], [2, 3, 3], [3, 5]]
>>> combinationSum([2], 1)
[]
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    candidates = sorted(candidates)

    def combination_sum(combination, i):

        s = sum(combination)

        if s == target:
            result.append(combination.copy())
            return

        if i >= len(candidates):
            return

        if s > target:
            return

        for j in range(i, len(candidates)):
            if s + candidates[j] <= target:
                combination_sum(combination + [candidates[j]], j)
            else:
                break

    combination_sum([], 0)
    return result
