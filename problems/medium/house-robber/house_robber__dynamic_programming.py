r"""
>>> from house_robber__dynamic_programming import rob
>>> rob([1, 2, 3, 1])
4
>>> rob([2, 7, 9, 3, 1])
12
"""

from typing import List

def rob(nums: List[int]) -> int:
    money = [0] * len(nums)
    for i, n in enumerate(nums):
        if i == 0:
            money[i] = n
        elif i == 1:
            money[i] = max(money[i - 1], n)
        else:
            money[i] = max(money[i - 1], n + money[i - 2])

    return money[-1]
