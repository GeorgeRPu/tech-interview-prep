r"""
>>> from combination_sum_ii__backtracking import combinationSum2
>>> sorted([sorted(c) for c in combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)])
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
>>> sorted([sorted(c) for c in combinationSum2([2, 5, 2, 1, 2], 5)])
[[1, 2, 2], [5]]
"""

from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    candidates = sorted(candidates)

    def combination_sum(combination, i):
        s = sum(combination)

        if s == target:
            result.append(combination.copy())
            return

        if s > target:
            return

        if i >= len(candidates):
            return

        for j in range(i, len(candidates)):
            if s + candidates[j] > target:
                break

            if j > i and candidates[j] == candidates[j - 1]:
                continue

            combination_sum(combination + [candidates[j]], j + 1)

    combination_sum([], 0)
    return result
