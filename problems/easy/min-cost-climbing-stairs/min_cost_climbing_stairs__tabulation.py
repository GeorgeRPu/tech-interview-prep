r"""
>>> from min_cost_climbing_stairs__tabulation import minCostClimbingStairs
>>> minCostClimbingStairs([10, 15, 20])
15
>>> minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
6
"""


def minCostClimbingStairs(cost: list[int]) -> int:
    """Return the minimum cost to reach the top of the staircase."""
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]
