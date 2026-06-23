r"""
>>> from koko_eating_bananas__binary_search import minEatingSpeed
>>> minEatingSpeed([3, 6, 7, 11], 8)
4
>>> minEatingSpeed([30, 11, 23, 4, 20], 5)
30
>>> minEatingSpeed([30, 11, 23, 4, 20], 6)
23
"""

import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)

    result = 0

    while left <= right:
        k = (left + right) // 2

        # calculate how long she takes to eat
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)

        if hours <= h:
            result = k
            right = k - 1
        else:
            left = k + 1

    return result
