r"""
>>> from target_sum__memoization import findTargetSumWays
>>> findTargetSumWays([1, 1, 1, 1, 1], 3)
5
>>> findTargetSumWays([1], 1)
1
"""


def findTargetSumWays(nums: list[int], target: int) -> int:
    memo = {}

    def target_sum_ways(i, t):
        if (i, t) in memo:
            return memo[(i, t)]

        if i == len(nums):
            memo[(i, t)] = 1 if t == 0 else 0
            return 1 if t == 0 else 0

        neg_ways = target_sum_ways(i + 1, t - nums[i])
        pos_ways = target_sum_ways(i + 1, t + nums[i])
        memo[(i + 1, t - nums[i])] = neg_ways
        memo[(i + 1, t + nums[i])] = pos_ways
        return neg_ways + pos_ways

    return target_sum_ways(0, target)
