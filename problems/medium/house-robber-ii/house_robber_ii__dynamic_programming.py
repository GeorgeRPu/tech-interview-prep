r"""
>>> from house_robber_ii__dynamic_programming import rob
>>> rob([2, 3, 2])
3
>>> rob([1, 2, 3, 1])
4
>>> rob([1, 2, 3])
3
"""

from typing import List

def rob(nums: List[int]) -> int:
    N = len(nums)

    if len(nums) == 1:
        return nums[0]

    money = [0] * (N - 1)
    money1 = [0] * (N - 1)
    for i, num in enumerate(nums[:-1]):
        if i == 0:
            money[i] = num
        elif i == 1:
            money[i] = max(money[i - 1], num)
        else:
            money[i] = max(money[i - 1], num + money[i - 2])

    for i, num in enumerate(nums[1:]):
        if i == 0:
            money1[i] = num
        elif i == 1:
            money1[i] = max(money1[i - 1], num)
        else:
            money1[i] = max(money1[i - 1], num + money1[i - 2])

    return max(money[-1], money1[-1])
